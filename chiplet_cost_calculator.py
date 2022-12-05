import math
import xml.etree.ElementTree as ET
#import csv
#import os
#import numpy as np
import matplotlib.pyplot as plt
#from sklearn import preprocessing, model_selection

# Import Constants File. To change default values, edit constants.py.
from constants import *

def interposer_cost(interposer_size):   # Interposer size is in mm^2
    return interposer_wafer_cost_per_mm2*interposer_size # Returned value is the cost for the interposer in USD

def assembly_time(number_chiplets,sim_bonding=simultaneous_bonding,t_placement=tplace,t_bonding=tbond,num_simult=place_group_size):
    n = number_chiplets/num_simult
    if sim_bonding:
        t = t_bonding + n*t_placement
    else:
        t = n*(t_bonding+t_placement)
    return t

def assembly_cost_per_second(machine_c=machine_cost,labor_c=labor_cost,machine_dep_t=machine_depreciation_time):
    return (labor_c+machine_c/machine_dep_t)/(365*24*60*60)

def assembly_cost(number_chiplets,interposer_size,sim_bonding=simultaneous_bonding,t_placement=tplace,t_bonding=tbond,machine_c=machine_cost,num_simult=place_group_size):
    cost = interposer_cost(interposer_size) + assembly_time(number_chiplets,sim_bonding,t_placement,t_bonding,num_simult)*assembly_cost_per_second(machine_c)
    return cost

def silicon_yield(chip_size,defect_density):
    defect_yield = (1+(defect_density*chip_size)/clustering_factor)**(-1*clustering_factor)
    return wafer_process_yield*defect_yield

def litho_cost_per_mm_sq(chip_size):
    chips_per_exposure = math.floor(reticle_area/chip_size)
    litho_cost_per_exposure = fraction_wafer_cost_litho*wafer_cost_per_mm2*reticle_area
    litho_cost = (litho_cost_per_exposure)/(chip_size*chips_per_exposure)
    return litho_cost

def cost_per_mm_sq(chip_size,defect_density,wafer_cost=wafer_40nm_cost):
    cost = litho_cost_per_mm_sq(chip_size) + (wafer_cost/wafer_area)*(1-fraction_wafer_cost_litho)
    cost = cost/silicon_yield(chip_size,defect_density)
    return cost

def testcase_cost_800(chiplet_size,defect_density,sim_bonding=simultaneous_bonding,t_placement=tplace,t_bonding=tbond,machine_c=machine_cost,num_simult=place_group_size,wafer_cost=wafer_40nm_cost):
    num_chiplets = math.floor(800/chiplet_size)
    chip_size = 800/num_chiplets
    chip_cost = num_chiplets*chip_size*cost_per_mm_sq(chip_size,defect_density,wafer_cost)
    interposer_size = num_chiplets*(math.sqrt(chip_size)+0.001*chip_separation)**2
    assm_cost = assembly_cost(num_chiplets,interposer_size,sim_bonding,t_placement,t_bonding,machine_c,num_simult)
    return chip_cost + assm_cost

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
