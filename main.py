# This file generates the plots shown in the paper.
# Results may differ from results in paper as additional parameters are added.

import chiplet_cost_calculator as c
import xml.etree.ElementTree as ET

# Read System Description
system = ET.parse('system.xml')

interposer = system.getroot().find('interposer').attrib
assembly_process_name = system.getroot().attrib['assembly_process']
n_chiplets = int(system.getroot().attrib['n_chiplets'])
quantity = int(system.getroot().attrib['quantity'])
if (system.getroot().attrib['multi_chip_reticle'] == "True"):
    multi_chip_reticle = True
else:
    multi_chip_reticle = False

chiplets = []
for child in system.getroot():
    if child.tag == 'chiplet':
        chiplets.append(child.attrib)

# Collect settings from the XML file.
config = ET.parse('tech.xml')

assembly_process_def = []
interposer_process_def = []
tech_process_def = []
for child in config.getroot():
    if child.tag == "interposer":
        interposer_process_def.append(child)
    elif child.tag == "assembly_process":
        assembly_process_def.append(child)
    elif child.tag == "technology":
        tech_process_def.append(child)

# Since there is only one process definition, select the correct process from the tech file here.
for p in assembly_process_def:
    if p.attrib['name'] == assembly_process_name:
        assembly_process = p.attrib

interposer_process_name = assembly_process['interposer']

# Since there is only one interposer, select the correct process from the tech file here.
for p in interposer_process_def:
    if p.attrib['name'] == interposer_process_name:
        interposer_process = p.attrib


re_cost = 0
interposer_cost = c.interposer_cost(interposer,interposer_process)
print(f"Interposer cost: {interposer_cost}")
assembly_time = c.assembly_time(n_chiplets,assembly_process)
print(f"Assembly time: {assembly_time}")
assembly_cost = c.assembly_cost(n_chiplets,interposer,interposer_process,assembly_process)
print(f"Assembly cost: {assembly_cost}")
re_cost += assembly_cost
present_technologies = []
n_pins = 0
for chiplet in chiplets:
    print(chiplet['name'])
    print(chiplet['tech'])
    n_pins += int(chiplet['inpins']) + int(chiplet['outputpins']) + int(chiplet['extinpins']) + int(chiplet['extoutputpins']) + int(chiplet['pwrpins'])
    for tech in tech_process_def:
        tech_count = 0
        if tech.attrib['name'] == chiplet['tech']:
            tech_count = tech_count + 1
            chip_cost = c.chip_cost(float(chiplet['area']),tech.attrib)
            print(f"Chip cost: {chip_cost}")
            continue
        if tech_count > 0:
            present_technologies.append((tech,tech_count))
    re_cost += chip_cost

assem_yield = c.assembly_yield(n_chiplets,n_pins,assembly_process)
re_cost = re_cost/assem_yield
print(f"Assembly yield: {assem_yield}")

print(f"Cost without NRE: {re_cost}")

nre_cost = c.interposer_nre_cost(interposer,interposer_process,quantity)
for technology,num in present_technologies:
    nre_cost = nre_cost + c.nre_cost(num,technology,quantity,multi_chip_reticle)

total_cost = nre_cost + re_cost

print(f"NRE cost: {nre_cost}")

print(f"Total cost: {total_cost}")


## Each chiplet could have a different technology node, so those will be selected from tech_process_def later.
#
#defect_densities = [0.004,0.002,0.0007]
#
## Reticle Fit Chip Area Costs
#reticle_size_result = {}
#reticle_size_result['x'] = [1,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800]
#reticle_size_result['count'] = 0
#reticle_size_result['labels'] = []
##[str(defect_densities[0]),str(defect_densities[1]),str(defect_densities[2])]
#reticle_size_result['y'] = []
#for defect_density in defect_densities:
#    reticle_size_result['y'].append([])
#    reticle_size_result['labels'].append(str(defect_density))
#    for chip_size in reticle_size_result['x']:
#        #reticle_size_result['y'][reticle_size_result['count']].append(c.litho_cost_per_mm_sq(chip_size))
#        reticle_size_result['y'][reticle_size_result['count']].append(c.cost_per_mm_sq(chip_size,defect_density))
#        #reticle_size_result['y'][reticle_size_result['count']].append(c.silicon_yield(chip_size,defect_density))
#    reticle_size_result['count'] += 1
#
#reticle_size_result['y_label'] = r'Cost per mm$^2$ (\$)'
#reticle_size_result['x_label'] = r'Chip Size (mm$^2$)'
#reticle_size_result['name'] = 'Cost per Area with Reticle Fit and Yield'
#
#c.plot_result(reticle_size_result)
#
#
## IO Cell Energy Per Bit for Inter-Chiplet Communication for Different IO Densities
#
#
## Percentage of Area Consumed by IO Cells for Different IO Densities
#
#
## Assembly Machine and Personnel Cost by Number of Chiplets
#assembly_cost_result = {}
#assembly_cost_result['x'] = range(1,17)
#assembly_cost_result['count'] = 0
#assembly_cost_result['labels'] = []
#assembly_cost_result['y'] = []
#bonding_time = 20
#for bonding in ['SB','IB']:
#    for machine_cost in [2000000,1000000,200000]:
#        for pick_and_place in [2,10]:
#            assembly_cost_result['y'].append([])
#            # This assumes 20 second bonding time in all cases.
#            for i in assembly_cost_result['x']:
#                sim_bonding = False
#                if bonding == 'SB':
#                    sim_bonding = True
#                assembly_cost_result['y'][assembly_cost_result['count']].append(c.assembly_cost(i,858,sim_bonding,pick_and_place,bonding_time,machine_cost))
#            assembly_cost_result['labels'].append(bonding + ",\$" + str(machine_cost) + "," + str(pick_and_place) + "," + str(bonding_time))
#            assembly_cost_result['count'] += 1
#
#assembly_cost_result['y_label'] = 'Cost of Assembly (USD)'
#assembly_cost_result['x_label'] = 'Number of Chiplets'
#assembly_cost_result['name'] = 'Assembly Machine and Personnel Cost by Number of Chiplets'
#
#c.plot_result(assembly_cost_result)
#
## Cost for Different Defect Densities at 40nm
#full_cost_result = {}
#full_cost_result['x'] = [1,2,4,5,8,10,16,20,25,32,50,80,100,160,200,400,800]
#full_cost_result['count'] = 0
#full_cost_result['labels'] = []
#full_cost_result['y'] = []
#defect_densities = [0.004,0.002,0.0007]
#for defect_density in defect_densities:
#    full_cost_result['y'].append([])
#    full_cost_result['labels'].append(defect_density)
#    for chiplet_size in full_cost_result['x']:
#        full_cost_result['y'][full_cost_result['count']].append(c.testcase_cost_800(chiplet_size,defect_density))
#    full_cost_result['count'] += 1
#
#full_cost_result['y_label'] = 'Cost per Assembled System (\$)'
#full_cost_result['x_label'] = r'Chiplet Size (mm$^2$)'
#full_cost_result['name'] = 'Cost for Different Defect Densities at 40nm'
#
#c.plot_result(full_cost_result)
#
## Costs for Different Bonding/Pick and Place Times and Machines
#machine_sweep_result = {}
#machine_sweep_result['x'] = [4,5,8,10,16,20,25,32,50,80,100,160,200]
#machine_sweep_result['count'] = 0
#machine_sweep_result['labels'] = []
#machine_sweep_result['y'] = []
#defect_density = 0.002
#pick_and_place_times = [10,20,30]
#bonding_times = [10,20]
#machine_costs = [2000000,1000000,200000]
#for pnp_t in pick_and_place_times:
#    for b_t in bonding_times:
#        for m_c in machine_costs:
#            machine_sweep_result['y'].append([])
#            machine_sweep_result['labels'].append(str(pnp_t)+"_"+str(b_t)+"_"+str(m_c))
#            for chiplet_size in machine_sweep_result['x']:
#                machine_sweep_result['y'][machine_sweep_result['count']].append(c.testcase_cost_800(chiplet_size,defect_density,False,pnp_t,b_t,m_c))
#            machine_sweep_result['count'] += 1
#
#machine_sweep_result['y_label'] = 'Cost per Assembled System (\$)'
#machine_sweep_result['x_label'] = r'Chiplet Size (mm$^2$)'
#machine_sweep_result['name'] = 'Cost for Different Bonding/Pick and Place Times and Machines'
#
#c.plot_result(machine_sweep_result)
#
## Cost for Simultaneous Bonding
#
#machine_sweep_sb_result = {}
#machine_sweep_sb_result['x'] = [4,5,8,10,16,20,25,32,50,80,100,160,200]
#machine_sweep_sb_result['count'] = 0
#machine_sweep_sb_result['labels'] = []
#machine_sweep_sb_result['y'] = []
#defect_density = 0.002
#pick_and_place_times = [10,20,30]
#bonding_times = [10,20]
#machine_costs = [2000000,1000000,200000]
#for pnp_t in pick_and_place_times:
#    for b_t in bonding_times:
#        for m_c in machine_costs:
#            machine_sweep_sb_result['y'].append([])
#            machine_sweep_sb_result['labels'].append(str(pnp_t)+"_"+str(b_t)+"_"+str(m_c))
#            for chiplet_size in machine_sweep_sb_result['x']:
#                machine_sweep_sb_result['y'][machine_sweep_sb_result['count']].append(c.testcase_cost_800(chiplet_size,defect_density,True,pnp_t,b_t,m_c))
#            machine_sweep_sb_result['count'] += 1
#
#machine_sweep_sb_result['y_label'] = 'Cost per Assembled System (\$)'
#machine_sweep_sb_result['x_label'] = r'Chiplet Size (mm$^2$)'
#machine_sweep_sb_result['name'] = 'Cost for Different Bonding/Pick and Place Times and Machines Simultaneous Bonding'
#
#c.plot_result(machine_sweep_sb_result)
#
## Costs for Different Levels for ESD Protection
#
#
## Costs for Assembled System in Different Technology Nodes
#
#machine_sweep_sb_result = {}
#machine_sweep_sb_result['x'] = [1,2,4,5,8,10,16,20,25,32,50,80,100,160,200,400,800]
#machine_sweep_sb_result['count'] = 0
#machine_sweep_sb_result['labels'] = []
#machine_sweep_sb_result['y'] = []
#defect_density = 0.002
#pick_and_place_times = [10]
#bonding_times = [20]
#machine_costs = [1000000]
#for pnp_t in pick_and_place_times:
#    for b_t in bonding_times:
#        for m_c in machine_costs:
#            machine_sweep_sb_result['y'].append([])
#            machine_sweep_sb_result['labels'].append(str(pnp_t)+"_"+str(b_t)+"_"+str(m_c))
#            for chiplet_size in machine_sweep_sb_result['x']:
#                machine_sweep_sb_result['y'][machine_sweep_sb_result['count']].append(c.testcase_cost_800(chiplet_size,defect_density,True,pnp_t,b_t,m_c))
#            machine_sweep_sb_result['count'] += 1
#
#machine_sweep_sb_result['y_label'] = 'Cost per Assembled System (\$)'
#machine_sweep_sb_result['x_label'] = r'Chiplet Size (mm$^2$)'
#machine_sweep_sb_result['name'] = 'Cost for Different Bonding/Pick and Place Times and Machines Simultaneous Bonding'
#
#c.plot_result(machine_sweep_sb_result)
#
## Optimal Chiplet Size by Technology
#
#tech_sweep_result = {}
#tech_sweep_result['x'] = [5,7,10,12,20,28,40,65,90]
#wafer_costs = [16988,9346,5992,3984,3677,2891,2274,1937,1650]
#x_vals = [1,2,4,5,8,10,16,20,25,32,50,57.1429,66.6666,72.7272,80,100,114.286,133.333,160,200,400,800]
#tech_sweep_result['count'] = 0
#tech_sweep_result['labels'] = []
#tech_sweep_result['y'] = []
#defect_densities = [0.004,0.002,0.0007]
#pick_and_place_times = [10]
#bonding_times = [20]
#machine_costs = [1000000]
#
#for defect_density in defect_densities:
#    tech_sweep_result['y'].append([])
#    tech_sweep_result['labels'].append('Defect Density = ' + str(defect_density))
#    i = 0
#    for tech in tech_sweep_result['x']:
#        min_tech = 0
#        min_y_val = 1000000000
#        for chiplet_size in x_vals:
#            #tech_sweep_result['labels'].append(str(pnp_t)+"_"+str(b_t)+"_"+str(m_c))
#            tmp = c.testcase_cost_800(chiplet_size,defect_density,wafer_cost=wafer_costs[i])
#            if (tmp < min_y_val):
#                min_y_val = tmp
#                min_tech = chiplet_size
#        tech_sweep_result['y'][tech_sweep_result['count']].append(min_tech)
#        i += 1
#    tech_sweep_result['count'] += 1
#
#tech_sweep_result['y_label'] = r'Lowest Cost Chiplet Size (mm$^2$)'
#tech_sweep_result['x_label'] = 'Technology Node (nm)'
#tech_sweep_result['name'] = 'Optimal Chiplet Sizes by Technology Node'
#
#c.plot_result(tech_sweep_result)
#
#
#
#
## Additional Power Consumed by Added Wire and ESD Capacitance
#
#
## Performance-Aware Yield
#
#
