import math
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Import Constants File. To change default values, edit constants.py.
from constants import *

# TODO: Add functions to check validity of the provided functions to give more informative error messages.

# Returns the interposer cost given interposer parameters and interposer process parameters.
def interposer_cost(interposer,interposer_process):   # Interposer size is in mm^2
    cost_per_mm2 = float(interposer_process["wafer_cost"])/(math.pi*((float(interposer_process["wafer_diameter"])/2)-float(interposer_process["edge_exclusion"]))**2)
    total_interposer_cost = cost_per_mm2*float(interposer["area"]) # Returned value is the cost for the interposer in USD
    return total_interposer_cost

# Returns the usable wafer area.
def wafer_area_eff(tech):
    usable_wafer_radius = (float(tech["wafer_diameter"])/2)-float(tech["edge_exclusion"])
    usable_wafer_area = math.pi*(usable_wafer_radius)**2
    return usable_wafer_area

# Returns the assmbly time required for the system.
def assembly_time(n_chiplets,assembly_process):
    num_bonding_groups = math.ceil(n_chiplets/int(assembly_process["bonding_group"]))
    bonding_time = num_bonding_groups*float(assembly_process["tbond"])
    num_picknplace_groups = math.ceil(n_chiplets/int(assembly_process["picknplace_group"]))
    picknplace_time = num_picknplace_groups*float(assembly_process["tplace"])
    time = bonding_time + picknplace_time
    return time

# Returns the assembly cost per second computed from labor costs and machine depreciation.
def assembly_cost_per_second(assembly_process):
    machine_cost_per_year = float(assembly_process["machine_cost"])/float(assembly_process["machine_lifetime_years"])
    total_cost_per_year = float(assembly_process["machine_labor_cost"]) + machine_cost_per_year
    num_seconds_in_year = 365*24*60*60
    assembly_cost_per_second = total_cost_per_year/num_seconds_in_year
    return assembly_cost_per_second

# Returns assembly cost. This includes the cost of the interposer and the bonding machine cost. All these costs are assumed to exist for the 2.5D system and not the monolithic SoC, so final packaging costs are not included as these would likely be similar between a 2.5D and a monolithic design.
def assembly_cost(n_chiplets,interposer,interposer_process,assembly_process):
    int_cost = interposer_cost(interposer,interposer_process)
    assem_time = assembly_time(n_chiplets,assembly_process)
    assem_cost_per_second = assembly_cost_per_second(assembly_process)
    cost = int_cost + assem_time*assem_cost_per_second
    return cost

# This computes the silicon yield for a certain chip size and technology node. This can be used for a monolithic design as well as a chiplet.
# Assembly yield is computed separately.
def silicon_yield(chip_size,tech):
    # Using the negative binomial model.
    defect_yield = (1+(float(tech["defect_density"])*chip_size)/float(tech["clustering_factor"]))**(-1*float(tech["clustering_factor"]))
    wafer_process_yield = float(tech["wafer_process_yield"])
    final_silicon_yield = wafer_process_yield*defect_yield
    return final_silicon_yield

# This computes the yield for the bonding and assembly process.
def assembly_yield(num_chips,num_pins,assembly_process):
    alignment_yield = float(assembly_process["alignment_yield"])**num_chips
    bonding_yield = float(assembly_process["bonding_yield"])**num_pins
    assembly_yield = alignment_yield*bonding_yield
    return assembly_yield

# This computes the litho cost penalty for a bad chip fit in the reticle. (This assumes aspect ratio of the chip is not fixed.)
def litho_cost_per_mm_sq(chip_size,tech):
    reticle_area = float(tech["reticle_x"])*float(tech["reticle_y"])
    chips_per_exposure = math.floor(reticle_area/chip_size)
    wafer_cost_per_mm2 = float(tech["wafer_cost"])/(wafer_area_eff(tech))
    litho_cost_per_exposure = float(tech["fraction_wafer_cost_litho"])*wafer_cost_per_mm2*reticle_area
    litho_cost = (litho_cost_per_exposure)/(chip_size*chips_per_exposure)
    return litho_cost

# This computes the cost per mm^2 for a certain chip size and technology accounting for the reticle fit in the above formula.
def cost_per_mm_sq(chip_size,tech):
    cost = litho_cost_per_mm_sq(chip_size,tech) + (float(tech["wafer_cost"])/(wafer_area_eff(tech)))*(1-float(tech["fraction_wafer_cost_litho"]))
    cost = cost/silicon_yield(chip_size,tech)
    return cost

# Find actual recurring chip cost.
def chip_cost(chip_size,tech):
    return chip_size*cost_per_mm_sq(chip_size,tech)

# NRE cost for interposer including design and mask.
def interposer_nre_cost(interposer,interposer_process,quantity):
    cost = float(interposer_process["nre_mask_cost"]) + float(interposer_process["design_cost"])*float(interposer["area"])
    ammortized = cost/quantity
    return ammortized

# NRE cost for chips not including the interposer.
def nre_cost(num_chips,total_area,tech,quantity,multi_chip_reticle):
    nre_cost = tech["design_cost"]*total_area
    if (multi_chip_reticle == "False"):
        return num_chips*nre_cost/quantity + tech["nre_mask_cost"]*num_chips/quantity
    else:
        # This considers that all chips can be fit within the same reticle. Add a check for this condition.
        return nre_cost/quantity + tech["nre_mask_cost"]/quantity

#def testcase_cost_800(chiplet_size,defect_density,sim_bonding=simultaneous_bonding,t_placement=tplace,t_bonding=tbond,machine_c=machine_cost,num_simult=place_group_size,wafer_cost=wafer_40nm_cost):
#    num_chiplets = math.floor(800/chiplet_size)
#    chip_size = 800/num_chiplets
#    chip_cost = num_chiplets*chip_size*cost_per_mm_sq(chip_size,defect_density,wafer_cost)
#    interposer_size = num_chiplets*(math.sqrt(chip_size)+0.001*chip_separation)**2
#    assm_cost = assembly_cost(num_chiplets,interposer_size,sim_bonding,t_placement,t_bonding,machine_c,num_simult)
#    return chip_cost + assm_cost

def plot_result(result):
    plt.figure(result['name'])
    x_value = result['x']
    x_label = result['x_label']
    y_label = result['y_label']
    #x_range = None
    #x_scale = "log"
    
    for i in range(result['count']):
        plt.plot(x_value, result['y'][i], label = result['labels'][i]) #, marker='x', markersize=8)
    #plt.plot(x_value, result['test_err'], label = 'test_error', marker='o', markersize=8)

    plt.xlabel(x_label, fontsize=12) 
    plt.ylabel(y_label, fontsize=12)
    plt.legend()
    plt.grid()
    #plt.xscale(x_scale)
    #plt.xlim(x_range)
    plt.show()
