import math
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

def assembly_cost(number_chiplets,interposer_size):
    cost = interposer_cost(interposer_size) + assembly_time(number_chiplets)*assembly_cost_per_s
    return cost


