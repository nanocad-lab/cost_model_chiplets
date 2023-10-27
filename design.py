# Define Design Class and Corresponding Subclasses
# This is meant to avoid passing the same set of parameters to every function in the partitioning code.

import numpy as np
import math
import sys
#import fiducciaMattheyses.run_params as params
import xml.etree.ElementTree as ET


# =========================================
# Wafer Process Class
# =========================================
# The class has the followin attributes:
#   name: The name of the wafer process.
#   wafer_diameter: The diameter of the wafer in mm.
#   edge_exclusion: The edge exclusion of the wafer in mm.
#   wafer_process_yield: The yield of the wafer process. Value should be between 0 and 1.
#   reticle_x: Reticle dimension in the x dimension in mm.
#   reticle_y: Reticle dimension in the y dimension in mm.
#   static: A boolean set true when the process is defined to prevent further changes.
# =========================================
# The class has the following methods.
# == Get/Set ==
#   get_name()
#   set_name(string)
#   get_wafer_diameter()
#   set_wafer_diameter(float)
#   get_edge_exclusion()
#   set_edge_exclusion(float)
#   get_wafer_process_yield()
#   set_wafer_process_yield(float)
#   get_reticle_x()
#   set_reticle_x(float)
#   get_reticle_y()
#   set_reticle_y(float)
#   get_static()
#   set_static()
# == Print ==
#   print_description(): Dumps values of all the parameters for inspection.
# =========================================

class WaferProcess:
    def __init__(self, name=None, wafer_diameter=None, edge_exclusion=None, wafer_process_yield=None, dicing_distance=None, reticle_x=None, reticle_y=None, static=True) -> None:
        self.name = name
        self.wafer_diameter = wafer_diameter
        self.edge_exclusion = edge_exclusion
        self.wafer_process_yield = wafer_process_yield
        self.dicing_distance = dicing_distance
        self.reticle_x = reticle_x
        self.reticle_y = reticle_y
        self.static = static
        if self.name == None or self.wafer_diameter == None or self.edge_exclusion == None or self.wafer_process_yield == None or self.reticle_x == None or self.reticle_y == None:
            print("Warning: Wafer Process not fully defined, setting to non-static.")
            self.static = False
            print("Parameters given for Wafer Process name " + str(self.name) + " are wafer_diameter = " + str(self.wafer_diameter) + ", edge_exclusion = " + str(self.edge_exclusion) + ", wafer_process_yield = " + str(self.wafer_process_yield) + ", reticle_x = " + str(self.reticle_x) + ", reticle_y = " + str(self.reticle_y) + ".")
        return

    # ===== Get/Set Functions =====

    def get_name(self) -> str:
        return self.name

    def set_name(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.name = value
            return 0

    def get_wafer_diameter(self) -> float:
        return self.wafer_diameter

    def set_wafer_diameter(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.wafer_diameter = value
            return 0

    def get_edge_exclusion(self) -> float:
        return self.edge_exclusion

    def set_edge_exclusion(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.edge_exclusion = value
            return 0
    
    def get_wafer_process_yield(self) -> float:
        return self.wafer_process_yield

    def set_wafer_process_yield(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            if value < 0.0 or value > 1.0:
                print("Error: Wafer process yield must be between 0 and 1.")
                return 1
            self.wafer_process_yield = value
            return 0

    def get_dicing_distance(self) -> float:
        return self.dicing_distance
    
    def set_dicing_distance(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.dicing_distance = value
            return 0
    
    def get_reticle_x(self) -> int:
        return self.reticle_x

    def set_reticle_x(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.reticle_x = value
            return 0

    def get_reticle_y(self) -> bool:
        return self.reticle_y
    
    def set_reticle_y(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.reticle_y = value
            return 0

    def get_static(self) -> bool:
        return self.static

    def set_static(self) -> int:
        if self.name == None or self.wafer_diameter == None or self.edge_exclusion == None or self.wafer_process_yield == None or self.reticle_x == None or self.reticle_y == None:
            print("Error: Attempt to set wafer process static without defining all parameters. Exiting...")
            sys.exit(1)
        self.static = True
        return 0

    # ===== End Get/Set Functions =====

    # ===== Print Functions =====

    def print_description(self) -> None:
        print("Wafer Process Name: " + self.get_name()
                + "\n\r\tWafer Diameter: " + str(self.get_wafer_diameter())
                + "\n\r\tEdge Exclusion: " + str(self.get_edge_exclusion())
                + "\n\r\tWafer Process Yield: " + str(self.get_wafer_process_yield())
                + "\n\r\tReticle X: " + str(self.get_reticle_x())
                + "\n\r\tReticle Y: " + str(self.get_reticle_y())
                + "\n\r\tStatic: " + str(self.get_static()))
        return

    # ===== End Print Functions =====


# =========================================
# IO Class
# =========================================
# The class has the following attributes:
#   type: The type of IO for this adjacency matrix. (Select from list of IO definitions.)
#   rx_area: The area of RX IOs in mm^2.
#   tx_area: The area of TX IOs in mm^2
#   shoreline: The shoreline of the IO in mm.
#   bandwidth: The bandwidth of the IO in Gbps.
#   wire_count: The number of wires in the IO.
#   bidirectional: Whether the IO is bidirectional or not.
#   energy_per_bit: The energy per bit of the IO in pJ/bit.
#   reach: The reach of the IO in mm.
#   static: A boolean set true when the IO is defined to prevent further changes.
# =========================================
# The class has the following methods.
# == Get/Set ==
#   get_type()
#   set_type(string)
#   get_rx_area()
#   set_rx_area(float)
#   get_tx_area()
#   set_tx_area(float)
#   get_shoreline()
#   set_shoreline(float)
#   get_bandwidth()
#   set_bandwidth(float)
#   get_wire_count()
#   set_wire_count(int)
#   get_bidirectional()
#   set_bidirectional(bool)
#   get_energy_per_bit()
#   set_energy_per_bit(float)
#   get_reach()
#   set_reach(float)
#   get_static()
#   set_static()
# == Print ==
#   print_description(): Dumps values of all the parameters for inspection.
# =========================================

class IO:
    def __init__(self, type=None, rx_area=None, tx_area=None, shoreline=None, bandwidth=None, wire_count=None, bidirectional=None, energy_per_bit=None, reach=None, static=True) -> None:
        self.type = type
        self.rx_area = rx_area
        self.tx_area = tx_area
        self.shoreline = shoreline
        self.bandwidth = bandwidth
        self.wire_count = wire_count
        if bidirectional == "True" or bidirectional == "true":
            self.bidirectional = True
        else:
            self.bidirectional = False
        self.bidirectional = bidirectional
        self.energy_per_bit = energy_per_bit
        self.reach = reach
        self.static = static
        if self.type == None or self.rx_area == None or self.tx_area == None or self.shoreline == None or self.bandwidth == None or self.wire_count == None or self.bidirectional == None or self.energy_per_bit == None or self.reach == None:
            print("Warning: IO not fully defined, setting to non-static.")
            self.static = False
            print("Parameters given for IO type " + str(self.type) + " are area = " + str(self.area) + ", shoreline = " + str(self.shoreline) + ", bandwidth = " + str(self.bandwidth) + ", wire_count = " + str(self.wire_count) + ".")
        return

    # ===== Get/Set Functions =====

    def get_type(self) -> str:
        return self.type

    def set_type(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.type = value
            return 0

    def get_rx_area(self) -> float:
        return self.rx_area

    def set_rx_area(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.rx_area = value
            return 0

    def get_tx_area(self) -> float:
        return self.tx_area

    def set_tx_area(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.tx_area = value
            return 0

    def get_shoreline(self) -> float:
        return self.shoreline

    def set_shoreline(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.shoreline = value
            return 0    
    
    def get_bandwidth(self) -> float:
        return self.bandwidth

    def set_bandwidth(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.bandwidth = value
            return 0
    
    def get_wire_count(self) -> int:
        return self.wire_count

    def set_wire_count(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.wire_count = value
            return 0

    def get_bidirectional(self) -> bool:
        return self.bidirectional
    
    def set_bidirectional(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            if value == "True" or value == "true":
                self.bidirectional = True
            else:
                self.bidirectional = False
            return 0

    def get_energy_per_bit(self) -> float:
        return self.energy_per_bit
    
    def set_energy_per_bit(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.energy_per_bit = value
            return 0

    def get_reach(self) -> float:
        return self.reach
    
    def set_reach(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static IO.")
            return 1
        else:
            self.reach = value
            return 0

    def get_static(self) -> bool:
        return self.static

    def set_static(self) -> int:
        if self.type == None or self.rx_area == None or self.tx_area == None or self.shoreline == None or self.bandwidth == None or self.wire_count == None or self.bidirectional == None or self.energy_per_bit == None or self.reach == None:
            print("Error: Attempt to set IO static without defining all parameters. Exiting...")
        self.static = True
        return 0

    # ===== End Get/Set Functions =====

    # ===== Print Functions =====

    def print_description(self) -> None:
        print("IO Type: " + str(self.get_type())
                + "\n\n\tRX Area: " + str(self.get_rx_area())
                + "\n\n\tTX Area: " + str(self.get_tx_area())
                + "\n\n\tShoreline: " + str(self.get_shoreline())
                + "\n\r\tBandwidth: " + str(self.get_bandwidth())
                + "\n\r\tWire Count: " + str(self.get_wire_count())
                + "\n\r\tBidirectional: " + str(self.get_bidirectional())
                + "\n\r\tEnergy Per Bit: " + str(self.get_energy_per_bit())
                + "\n\n\tStatic: " + str(self.static))
        return

    # ===== End Print Functions =====


# =========================================
# Layer Class
# =========================================
# The class consists of the following attributes:
#   name: The name of the layer.
#   active: Whether the layer is active or not.
#   cost_per_mm2: The cost per mm^2 of the layer.
#   defect_density: The defect density of the layer.
#   critical_area_ratio: The critical area ratio of the layer.
#   clustering_factor: The clustering factor of the layer.
#   litho_percent: The litho percent of the layer.
#   mask_cost: The mask cost of the layer.
#   stitching_yield: The stitching yield of the layer.
#   static: A boolean set true when the layer is defined to prevent further changes.
# =========================================
# The class has the following methods.
# == Get/Set ==
#   get_name()
#   set_name(string)
#   get_active()
#   set_active(bool)
#   get_cost_per_mm2()
#   set_cost_per_mm2(float)
#   get_defect_density()
#   set_defect_density(float)
#   get_critical_area_ratio()
#   set_critical_area_ratio(float)
#   get_clustering_factor()
#   set_clustering_factor(float)
#   get_litho_percent()
#   set_litho_percent(float)
#   get_mask_cost()
#   set_mask_cost(float)
#   get_stitching_yield()
#   set_stitching_yield(float)
#   get_static()
#   set_static()
# == Print ==
#   print_description(): Dumps values of all the parameters for inspection.
# == Computation ==
#   layerYield(float): Computes the yield of the layer given the area of the layer.
#   reticleUtilization(float,float,float): Computes the reticle utilization given the area of the layer, the reticle x dimension, and the reticle y dimension.
#   layerCost(float,float,float): Computes the cost of the layer given the area of the layer, the reticle x dimension, and the reticle y dimension.
# =========================================

class Layer:
    def __init__(self, name=None, active=None, cost_per_mm2=None, defect_density=None, critical_area_ratio=None, clustering_factor=None, litho_percent=None, mask_cost=None, stitching_yield=None, static=True) -> None:
        self.name = name
        self.active = active
        self.cost_per_mm2 = cost_per_mm2
        self.defect_density = defect_density
        self.critical_area_ratio = critical_area_ratio
        self.clustering_factor = clustering_factor
        self.litho_percent = litho_percent
        self.mask_cost = mask_cost
        self.stitching_yield = stitching_yield
        self.static = static
        if self.name == None or self.active == None or self.cost_per_mm2 == None or self.defect_density == None or self.critical_area_ratio == None or self.clustering_factor == None or self.litho_percent == None or self.mask_cost == None or self.stitching_yield == None:
            print("Warning: Layer not fully defined. Setting non-static.")
            self.static = False
            print("IO " + self.name + " has parameters active = " + str(self.active) + ", cost_per_mm2 = " + str(self.cost_per_mm2) + ", defect_density = " + str(self.defect_density) + ", critical_area_ratio = " + str(self.critical_area_ratio) + ", litho_percent = " + str(self.litho_percent) + ", mask_cost = " + str(self.mask_cost) + ", stitching_yield = " + str(self.stitching_yield) + ".")
        return

    # =========== Get/Set Functions ===========

    def get_name(self) -> str:
        return self.name

    def set_name(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.name = value
            return 0

    def get_active(self) -> bool:
        return self.active

    def set_active(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.active = value
            return 0

    def get_cost_per_mm2(self) -> float:
        return self.cost_per_mm2

    def set_cost_per_mm2(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.cost_per_mm2 = value
            return 0

    def get_defect_density(self) -> float:
        return self.defect_density

    def set_defect_density(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.defect_density = value
            return 0

    def get_critical_area_ratio(self) -> float:
        return self.critical_area_ratio

    def set_critical_area_ratio(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.critical_area_ratio = value
            return 0

    def get_clustering_factor(self) -> float:
        return self.clustering_factor

    def set_clustering_factor(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.clustering_factor = value
            return 0

    def get_litho_percent(self) -> float:
        return self.litho_percent
    
    def set_litho_percent(self, value) -> int: 
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.litho_percent = value
            return 0

    def get_mask_cost(self) -> float:
        return self.mask_cost

    def set_mask_cost(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.mask_cost = value
            return 0
    
    def get_stitching_yield(self) -> float:
        return self.stitching_yield

    def set_stitching_yield(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static layer.")
            return 1
        else:
            self.stitching_yield = value
            return 0

    def get_static(self) -> bool:
        return self.static 

    def set_static(self) -> int: # The static variable should act somewhat like a latch, when it is set, it should not get unset.
        if self.name == None or self.active == None or self.cost_per_mm2 == None or self.defect_density == None or self.critical_area_ratio == None or self.clustering_factor == None or self.litho_percent == None or self.mask_cost == None or self.stitching_yield == None:
            print("Error: Attempt to set layer static without defining all parameters. Exiting...")
        self.static = True
        return 0

    # ======== End of Get/Set Functions ========

    # =========== Print Functions ==============

    def print_description(self) -> None:
        print("Layer " + self.name + " has parameters \n\r\t active = " + str(self.active) 
                + "\n\r\t cost_per_mm2 = " + str(self.cost_per_mm2)
                + "\n\r\t defect_density = " + str(self.defect_density)
                + "\n\r\t critical_area_ratio = " + str(self.critical_area_ratio)
                + "\n\r\t clustering_factor = " + str(self.clustering_factor)
                + "\n\r\t mask_cost = " + str(self.mask_cost)
                + "\n\r\t stitching_yield = " + str(self.stitching_yield)
                + "\n\r\t static = " + str(self.static) + ".")
        return  

    # ======== End of Print Functions ==========

    # ========== Computation Functions =========

    def layerYield(self,area) -> float:
        num_stitches = 0
        defect_yield = (1+(self.defect_density*area*self.critical_area_ratio)/self.clustering_factor)**(-1*self.clustering_factor)
        stitching_yield = self.stitching_yield**num_stitches
        final_layer_yield = stitching_yield*defect_yield
        return final_layer_yield

    def reticleUtilization(self,area,reticle_x,reticle_y) -> float:
        reticle_area = reticle_x*reticle_y
        # If the area is larger than the reticle area, this requires stitching. To get the reticle utilization,
        #  increase the reticle area to the lowest multiple of the reticle area that will fit the stitched chip.
        while reticle_area < area:
            reticle_area += reticle_x*reticle_y
        number_chips_in_reticle = reticle_area//area
        unutilized_reticle = (reticle_area) - number_chips_in_reticle*area
        reticle_utilization = (reticle_area - unutilized_reticle)/(reticle_area)
        return reticle_utilization
        
    def layerCost(self,area,wafer_process) -> float:
        wafer_diameter = wafer_process.get_wafer_diameter()
        edge_exclusion = wafer_process.get_edge_exclusion()
        reticle_x = wafer_process.get_reticle_x()
        reticle_y = wafer_process.get_reticle_y()
        # TODO: Replace cost_per_mm2 with a function that takes the litho cost and reticle size into account.
        layer_cost = area*self.compute_cost_per_mm2(area,wafer_process)
        # Edge case to avoid division by zero.
        if (self.litho_percent == 0.0):
            reticle_utilization = 1.0
        else:
            reticle_utilization = self.reticleUtilization(area,reticle_x,reticle_y)
        
        layer_cost = layer_cost*(1-self.litho_percent) + (layer_cost*self.litho_percent)/reticle_utilization
        return layer_cost

    def compute_cost_per_mm2(self, square_area, wafer_process) -> float:
        wafer_diameter = wafer_process.get_wafer_diameter()
        edge_exclusion = wafer_process.get_edge_exclusion()
        dicing_distance = wafer_process.get_dicing_distance()
        # Compute the number of squares that fit in the circular wafer.
        usable_wafer_diameter = wafer_diameter - 2*edge_exclusion
        square_side = math.sqrt(square_area) + dicing_distance

        # I approximate this by assuming there are two possibilities for the best way to pack squares in the circle.
        #  1. The squares are centered on the diameter line of the circle.
        #  2. The squares are above and below the diameter line of the circle.

        # Case 1
        num_squares_case_1 = 0
        # Compute the length of a chord that intersects the circle half the square's side length away from the center of the circle.
        row_chord_height = square_side/2
        chord_length = math.sqrt((usable_wafer_diameter/2)**2 - (row_chord_height)**2)
        # Compute the number of squares that fit along the chord length.
        num_squares_case_1 += math.floor(chord_length/square_side)
        row_chord_height += square_side
        while row_chord_height < usable_wafer_diameter/2:
            # Compute the length of a chord that intersects the circle half the square's side length away from the center of the circle.
            chord_length = math.sqrt((usable_wafer_diameter/2)**2 - (row_chord_height)**2)
            num_squares_case_1 += 2*math.floor(chord_length/square_side)
            row_chord_height += square_side

        # Case 2
        num_squares_case_2 = 0
        # Compute the length of a chord that intersects the circle the square's side length away from the center of the circle.
        row_chord_height = square_side
        chord_length = math.sqrt((usable_wafer_diameter/2)**2 - (row_chord_height)**2)
        num_squares_case_2 += 2*math.floor(chord_length/square_side)
        row_chord_height += square_side
        while row_chord_height < usable_wafer_diameter/2:
            # Compute the length of a chord that intersects the circle half the square's side length away from the center of the circle.
            chord_length = math.sqrt((usable_wafer_diameter/2)**2 - (row_chord_height)**2)
            num_squares_case_2 += 2*math.floor(chord_length/square_side)
            row_chord_height += square_side
        
        # Find the maximum of the two cases.
        num_squares = max(num_squares_case_1, num_squares_case_2)

        # Compute the cost per mm^2.
        used_area = num_squares*square_area
        circle_area = math.pi*(wafer_diameter/2)**2
        cost_per_mm2 = self.cost_per_mm2*circle_area/used_area
        return cost_per_mm2

    # ===== End of Computation Functions =======


# =========================================
# Assembly Definition Class
# =========================================
# The class has attributes:
#   name: The name of the assembly process.
#   machine_cost_list: The cost of the machine for each year of its lifetime.
#   machine_lifetime_list: The lifetime of the machine in years.
#   machine_uptime_list: The uptime of the machine in hours per year.
#   technician_yearly_cost_list: The cost of the technician for each year of the machine's lifetime.
#   materials_cost_per_mm2: The cost of the materials per mm^2 of the assembly.
#   assembly_type: The type of assembly process. (Select from list of assembly definitions.)
#   picknplace_time: The time it takes to pick and place a die in seconds.
#   picknplace_group: The number of dies that can be picked and placed at once.
#   bonding_time: The time it takes to bond a die in seconds.
#   bonding_group: The number of dies that can be bonded at once.
#   dieSeparation: The distance between the dies in mm.
#   edgeExclusion: The distance from the edge of the wafer to the first die in mm.
#   max_pad_current_density: The maximum current density of the pads in mA/mm^2.
#   bonding_pitch: The pitch of the bonding pads in mm.
#   alignment_yield: The yield of the alignment process.
#   bonding_yield: The yield of the bonding process.
#   dielectric_bond_defect_density: The defect density of the dielectric bond.
#   static: A boolean set true when the assembly process is defined to prevent further changes.
# =========================================
# The class has the following methods.
# == Get/Set ==
#   get_name()
#   set_name(string)
##   get_machine_cost_list_len()
##   get_machine_cost_list()
##   set_machine_cost_list(list)
##   get_machine_cost(int)
##   set_machine_cost(int,float)
##   get_machine_lifetime_list_len()
##   get_machine_lifetime_list()
##   set_machine_lifetime_list(list)
##   get_machine_lifetime(int)
##   set_machine_lifetime(int,float)
##   get_machine_uptime_list_len()
##   get_machine_uptime_list()
##   set_machine_uptime_list(list)
##   get_machine_uptime(int)
##   set_machine_uptime(int,float)
##   get_technician_yearly_cost_list_len()
##   get_technician_yearly_cost_list()
##   set_technician_yearly_cost_list(list)
##   get_technician_yearly_cost(int)
##   set_technician_yearly_cost(int,float)
#   get_materials_cost_per_mm2()
#   set_materials_cost_per_mm2(float)
#   get_assembly_type()
#   set_assembly_type(string)
#   get_picknplace_machine_cost()
#   set_picknplace_machine_cost(float)
#   get_picknplace_machine_lifetime()
#   set_picknplace_machine_lifetime(float)
#   get_picknplace_machine_uptime()
#   set_picknplace_machine_uptime(float)
#   get_picknplace_technician_yearly_cost()
#   set_picknplace_technician_yearly_cost(float)
#   get_picknplace_time()
#   set_picknplace_time(float)
#   get_picknplace_group()
#   set_picknplace_group(int)
#   get_bonding_machine_cost()
#   set_bonding_machine_cost(float)
#   get_bonding_machine_lifetime()
#   set_bonding_machine_lifetime(float)
#   get_bonding_machine_uptime()
#   set_bonding_machine_uptime(float)
#   get_bonding_technician_yearly_cost()
#   set_bonding_technician_yearly_cost(float)
#   get_bonding_time()
#   set_bonding_time(float)
#   get_bonding_group()
#   set_bonding_group(int)
#   get_dieSeparation()
#   set_dieSeparation(float)
#   get_edgeExclusion()
#   set_edgeExclusion(float)
#   get_max_pad_current_density()
#   set_max_pad_current_density(float)
#   get_bonding_pitch()
#   set_bonding_pitch(float)
#   get_alignment_yield()
#   set_alignment_yield(float)
#   get_bonding_yield()
#   set_bonding_yield(float)
#   get_dielectric_bond_defect_density()
#   set_dielectric_bond_defect_density(float)
#   get_static()
#   set_static()
# == Print ==
#   print_description(): Dumps values of all the parameters for inspection.
# == Other ==
#   compute_picknplace_time(int): Computes the time it takes to pick and place a given number of dies.
#   compute_bonding_time(int): Computes the time it takes to bond a given number of dies.
#   assembly_time(float): Computes the assembly time given the area of the die in mm^2.
#   compute_assembly_cost_per_second(): Computes the cost per second of the assembly process.
#   assembly_cost(float): Computes the cost of the assembly process given the area of the die in mm^2.
#   assembly_yield(float): Computes the yield of the assembly process given the area of the die in mm^2.
# =========================================

class Assembly:
    def __init__(self, name="", materials_cost_per_mm2=None, assembly_type="", picknplace_machine_cost=None, picknplace_machine_lifetime=None, picknplace_machine_uptime=None, picknplace_technician_yearly_cost=None, picknplace_time=None, picknplace_group=None, bonding_machine_cost=None, bonding_machine_lifetime=None, bonding_machine_uptime=None, bonding_machine_technician_yearly_cost=None, bonding_time=None, bonding_group=None, dieSeparation=None, edgeExclusion=None, max_pad_current_density=None, bonding_pitch=None, alignment_yield=None, bonding_yield=None, dielectric_bond_defect_density=None, static=True) -> None:
#    def __init__(self, name="", machine_cost_list=[], machine_lifetime_list=[], machine_uptime_list=[], technician_yearly_cost_list=[], materials_cost_per_mm2=None, assembly_type="", picknplace_time=None, picknplace_group=None, bonding_time=None, bonding_group=None, dieSeparation=None, edgeExclusion=None, max_pad_current_density=None, bonding_pitch=None, alignment_yield=None, bonding_yield=None, dielectric_bond_defect_density=None, static=True) -> None:
        self.valid_assembly_types = ["D2D", "D2W", "W2W"]
        self.name = name
#        self.machine_cost_list = machine_cost_list
#        self.machine_lifetime_list = machine_lifetime_list
#        self.machine_uptime_list = machine_uptime_list
#        self.technician_yearly_cost_list = technician_yearly_cost_list
        self.materials_cost_per_mm2 = materials_cost_per_mm2
        if assembly_type == "":
            # print("Setting assembly type to default: " + self.valid_assembly_types[0] + ".")
            self.assembly_type = self.valid_assembly_types[0]
        else:
            self.assembly_type = assembly_type
        self.picknplace_machine_cost = picknplace_machine_cost
        self.picknplace_machine_lifetime = picknplace_machine_lifetime
        self.picknplace_machine_uptime = picknplace_machine_uptime
        self.picknplace_technician_yearly_cost = picknplace_technician_yearly_cost
        self.picknplace_time = picknplace_time
        self.picknplace_group = picknplace_group
        self.bonding_machine_cost = bonding_machine_cost
        self.bonding_machine_lifetime = bonding_machine_lifetime
        self.bonding_machine_uptime = bonding_machine_uptime
        self.bonding_machine_technician_yearly_cost = bonding_machine_technician_yearly_cost
        self.bonding_time = bonding_time
        self.bonding_group = bonding_group
        self.dieSeparation = dieSeparation                # Given Parameter
        self.edgeExclusion = edgeExclusion                # Given Parameter
        self.max_pad_current_density = max_pad_current_density  # Given Parameter
        self.bonding_pitch = bonding_pitch
        self.picknplace_cost_per_second = None
        self.bonding_cost_per_second = None
        self.bonding_yield = bonding_yield
        self.alignment_yield = alignment_yield
        self.dielectric_bond_defect_density = dielectric_bond_defect_density
        self.static = static
        if self.name == "" or self.machine_cost_list == [] or self.machine_lifetime_list == [] or self.machine_uptime_list == [] or self.technician_yearly_cost_list == [] or self.materials_cost_per_mm2 == None or self.assembly_type == "" or self.picknplace_time == None or self.picknplace_group == None or self.bonding_time == None or self.bonding_group == None:
            # print("Warning: Assembly not fully defined. Setting non-static.")
            self.static = False
            # print("Assembly process " + self.name + " has parameters machine_cost_list = " + str(self.machine_cost_list) + ", machine_lifetime_list = " + str(self.machine_lifetime_list) + ", machine_uptime_list = " + str(self.machine_uptime_list) + ", technician_yearly_cost_list = " + str(self.technician_yearly_cost_list) + ", materials_cost_per_mm2 = " + str(self.materials_cost_per_mm2) + ", assembly_type = " + self.assembly_type + ", picknplace_time = " + str(self.picknplace_time) + ", picknplace_group = " + str(self.picknplace_group) + ", bonding_time = " + str(self.bonding_time) + ", bonding_group = " + str(self.bonding_group) + ".")
        else:
            self.compute_picknplace_cost_per_second()
            self.compute_bonding_cost_per_second()

        
        if self.assembly_type not in self.valid_assembly_types:
            print("Error: Assembly type " + self.assembly_type + " is not valid.")
            print("Valid assembly types are: " + str(self.valid_assembly_types))
            self.static = False
        
        return

    # ====== Get/Set Functions ======

    def get_name(self) -> str:
        return self.name

    def set_name(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.name = value
            return 0
    
#    def get_machine_cost_list_len(self) -> int:
#        return len(self.machine_cost_list)
#
#    def get_machine_cost_list(self) -> list:
#        return self.machine_cost_list
#
#    def set_machine_cost_list(self, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.machine_cost_list = value
#            return 0
#    
#    def get_machine_cost(self, index) -> float:
#        return self.machine_cost_list[index]
#
#    def set_machine_cost(self, index, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.machine_cost_list[index] = value
#            return 0
#
#    def set_machine_lifetime_list(self, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.machine_lifetime_list = value
#            return 0
#    
#    def get_machine_lifetime(self, index) -> float:
#        return self.machine_lifetime_list[index]
#
#    def set_machine_lifetime(self, index, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.machine_lifetime_list[index] = value
#            return 0
#    
#    def get_machine_uptime_list_len(self) -> int:
#        return len(self.machine_uptime_list)
#
#    def get_machine_uptime_list(self) -> list:
#        return self.machine_uptime_list
#
#    def set_machine_uptime_list(self, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.machine_uptime_list = value
#            return 0
#    
#    def get_machine_uptime(self, index) -> float:
#        return self.machine_uptime_list[index]
#
#    def set_machine_uptime(self, index, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.machine_uptime_list[index] = value
#            return 0
#
#    def get_technician_yearly_cost_list_len(self) -> int:
#        return len(self.technician_yearly_cost_list)
#
#    def get_technician_yearly_cost_list(self) -> list:
#        return self.technician_yearly_cost_list
#
#    def set_technician_yearly_cost_list(self, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.technician_yearly_cost_list = value
#            return 0
#    
#    def get_technician_yearly_cost(self, index) -> float:
#        return self.technician_yearly_cost_list[index]
#
#    def set_technician_yearly_cost(self, index, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static assembly process.")
#            return 1
#        else:
#            self.technician_yearly_cost_list[index] = value
#            return 0
    
    def get_materials_cost_per_mm2(self) -> float:
        return self.materials_cost_per_mm2

    def set_materials_cost_per_mm2(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.materials_cost_per_mm2 = value
            return 0
    
    def get_assembly_type(self) -> str:
        return self.assembly_type

    def set_assembly_type(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        elif (value not in self.valid_assembly_types):
            print("Error: Invalid assembly type.")
            return 1
        else:
            self.assembly_type = value
            return 0
    
    def get_picknplace_machine_cost(self) -> float:
        return self.picknplace_machine_cost
    
    def set_picknplace_machine_cost(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.picknplace_machine_cost = value
            return 0

    def get_picknplace_machine_lifetime(self) -> float:
        return self.picknplace_machine_lifetime
    
    def set_picknplace_machine_lifetime(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.picknplace_machine_lifetime = value
            return 0
        
    def get_picknplace_machine_uptime(self) -> float:
        return self.picknplace_machine_uptime
    
    def set_picknplace_machine_uptime(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.picknplace_machine_uptime = value
            return 0 

    def get_picknplace_technician_yearly_cost(self) -> float:
        return self.picknplace_technician_yearly_cost
    
    def set_picknplace_technician_yearly_cost(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.picknplace_technician_yearly_cost = value
            return 0
    
    def get_picknplace_time(self) -> float:
        return self.picknplace_time

    def set_picknplace_time(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.picknplace_time = value
            return 0

    def get_picknplace_group(self) -> str:
        return self.picknplace_group

    def set_picknplace_group(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.picknplace_group = value
            return 0

    def get_bonding_machine_cost(self) -> float:
        return self.bonding_machine_cost
    
    def set_bonding_machine_cost(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.bonding_machine_cost = value
            return 0
        
    def get_bonding_machine_lifetime(self) -> float:
        return self.bonding_machine_lifetime
    
    def set_bonding_machine_lifetime(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.bonding_machine_lifetime = value
            return 0

    def get_bonding_machine_uptime(self) -> float:
        return self.bonding_machine_uptime

    def set_bonding_machine_uptime(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.bonding_machine_uptime = value
            return 0
 
    def get_bonding_technician_yearly_cost(self) -> float:
        return self.bonding_machine_technician_yearly_cost
    
    def set_bonding_technician_yearly_cost(self, value) -> float:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.bonding_machine_technician_yearly_cost = value
            return 0

    def get_bonding_time(self) -> float:
        return self.bonding_time

    def set_bonding_time(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.bonding_time = value
            return 0

    def get_bonding_group(self) -> str:
        return self.bonding_group

    def set_bonding_group(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static assembly process.")
            return 1
        else:
            self.bonding_group = value
            return 0

    def get_die_separation(self) -> float:
        return self.die_separation
    
    def set_die_separation(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.die_separation = value
            return 0
        
    def get_edge_exclusion(self) -> float:
        return self.edge_exclusion
    
    def set_edge_exclusion(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.edge_exclusion = value
            return 0

    def get_bonding_pitch(self) -> float:
        return self.bonding_pitch
    
    def set_bonding_pitch(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.bonding_pitch = value
            return 0

    def get_max_pad_current_density(self) -> float:
        return self.max_pad_current_density
    
    def set_max_pad_current_density(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.max_pad_current_density = value
            return 0

    def get_power_per_pad(self,core_voltage) -> float:
        pad_area = math.pi*(self.bonding_pitch/4)**2
        current_per_pad = self.max_pad_current_density*pad_area
        return current_per_pad*core_voltage

    def get_alignment_yield(self) -> float:
        return self.alignment_yield
    
    def set_alignment_yield(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.alignment_yield = value
            return 0
        
    def get_bonding_yield(self) -> float:
        return self.bonding_yield
    
    def set_bonding_yield(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.bonding_yield = value
            return 0

    def get_dielectric_bond_defect_density(self) -> float:
        return self.dielectric_bond_defect_density
    
    def set_dielectric_bond_defect_density(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.dielectric_bond_defect_density = value
            return 0

    def get_picknplace_cost_per_second(self) -> float:
        if self.picknplace_cost_per_second == None:
            self.compute_picknplace_cost_per_second()
        return self.picknplace_cost_per_second
    
    def set_picknplace_cost_per_second(self) -> int:
        self.picknplace_cost_per_second = self.compute_picknplace_cost_per_second()
        return 0

    def get_bonding_cost_per_second(self) -> float:
        if self.bonding_cost_per_second == None:
            self.compute_bonding_cost_per_second()
        return self.bonding_cost_per_second
    
    def set_bonding_cost_per_second(self) -> int:
        self.bonding_cost_per_second = self.compute_bonding_cost_per_second()
        return 0

    def get_static(self) -> bool:
        return self.static    

    def set_static(self) -> int:
        self.static = True
        return 0 

    # ===== End of Get/Set Functions =====

    # ===== Print Functions =====

    def print_description(self):
        print("Assembly Process Description:")
        print("\tAssembly Type: " + self.get_assembly_type())
        print("\tPick and Place Group: " + str(self.get_picknplace_group()))
        print("\tPick and Place Time: " + str(self.get_picknplace_time()))
        print("\tBonding Group: " + str(self.get_bonding_group()))
        print("\tBonding Time: " + str(self.get_bonding_time()))
        print("\tMaterials Cost per mm2: " + str(self.get_materials_cost_per_mm2()))
        print("\tMachine Cost is " + str(self.get_picknplace_machine_cost()) + " for the picknplace machine and " + str(self.get_bonding_machine_cost()) + " for the bonding machine.")
        print("\tTechnician Yearly Cost is " + str(self.get_picknplace_technician_yearly_cost()) + " for picknplace and " + str(self.get_bonding_technician_yearly_cost()) + " for bonding.")
        print("\tMachine Uptime is " + str(self.get_picknplace_machine_uptime()) + " for the picknplace machine and " + str(self.get_bonding_machine_uptime()) + " for the bonding machine.")
        print("\tMachine Lifetime is " + str(self.get_picknplace_machine_lifetime()) + " for the picknplace machine and " + str(self.get_bonding_machine_lifetime()) + " for the bonding machine.")
        return

    # ===== End of Print Functions =====

    # ===== Other Functions =====

    def compute_picknplace_time(self, n_chips):
        picknplace_steps = math.ceil(n_chips/self.picknplace_group)
        time = self.picknplace_time*picknplace_steps
        return time
    
    def compute_bonding_time(self, n_chips):
        bonding_steps = math.ceil(n_chips/self.bonding_group)
        time = self.bonding_time*bonding_steps
        return time
    
    def assembly_time(self, n_chips):
        time = self.compute_picknplace_time() + self.compute_bonding_time()
        return time

    def compute_picknplace_cost_per_second(self):
        machine_cost_per_year = self.get_picknplace_machine_cost()/self.get_picknplace_machine_lifetime()
        technician_cost_per_year = self.get_picknplace_technician_yearly_cost()
        picknplace_cost_per_year = machine_cost_per_year + technician_cost_per_year
        picknplace_cost_per_second = picknplace_cost_per_year/(365*24*60*60)*self.get_picknplace_machine_uptime()
        self.picknplace_cost_per_second = picknplace_cost_per_second
        return picknplace_cost_per_second
    
    def compute_bonding_cost_per_second(self):
        machine_cost_per_year = self.get_bonding_machine_cost()/self.get_bonding_machine_lifetime()
        technician_cost_per_year = self.get_bonding_technician_yearly_cost()
        bonding_cost_per_year = machine_cost_per_year + technician_cost_per_year
        bonding_cost_per_second = bonding_cost_per_year/(365*24*60*60)*self.get_bonding_machine_uptime()
        self.bonding_cost_per_second = bonding_cost_per_second
        return bonding_cost_per_second

#    def compute_assembly_cost_per_second(self):
#        machine_cost_per_year = 0
#        # TODO: Add a list for proportion of time spend on each machine.
#        for i in range(len(self.machine_cost_list)):
#            machine_cost_per_year += self.machine_cost_list[i]/(self.machine_uptime_list[i]*self.machine_lifetime_list[i])
#        technician_cost_per_year = 0
#        for i in range(len(self.technician_yearly_cost_list)):
#            technician_cost_per_year += self.technician_yearly_cost_list[i]
#        assembly_cost_per_year = machine_cost_per_year + technician_cost_per_year
#        assembly_cost_per_second = assembly_cost_per_year/(365*24*60*60)
#        return assembly_cost_per_second

    def assembly_cost(self, n_chips, n_critical_bonds, area):
        # assembly_cost is a combination of the cost for machine and technician time and the materials cost.
        # assembly_cost = self.get_assembly_cost_per_second()*self.assembly_time(n_chips)
        assembly_cost = self.get_picknplace_cost_per_second()*self.compute_picknplace_time(n_chips) + self.get_bonding_cost_per_second()*self.compute_bonding_time(n_chips)

        #assembly_yield = self.assembly_yield(n_chips, n_critical_bonds, area)

        #assembly_cost = assembly_cost/assembly_yield

        return assembly_cost

    def assembly_yield(self, n_chips, n_bonds, area):
        assem_yield = 1.0
        assem_yield *= self.alignment_yield**n_chips
        assem_yield *= self.bonding_yield**n_bonds

        # If hybrid bonding, there is some yield impact of the dielectric bond.
        # This uses a defect density and area number which approximates the negative binomial yield model with no clustering.
        dielectric_bond_area = area
        dielectric_bond_yield = 1 - self.get_dielectric_bond_defect_density()*dielectric_bond_area
        assem_yield *= dielectric_bond_yield

        return assem_yield

    # ===== End of Other Functions =====

# Test Definition Class
# The class has attributes:
#   name: string
#   static: boolean
# The class has methods:
#   get_name: returns name
#   set_name: sets name
#   get_static: returns static
#   set_static: sets static to True
class Test:
    def __init__(self, name=None, test_self=None, test_assembly=None, test_quality_param=None, defect_coverage=None, die_numbers=None, test_cost_per_mm2=None, pattern_count=None, static=True) -> None:
        self.name = name
        self.static = static
        self.test_self = test_self
        self.test_assembly = test_assembly
        self.test_quality_param = test_quality_param
        self.defect_coverage = defect_coverage
        self.die_numbers = die_numbers
        self.test_cost_per_mm2 = test_cost_per_mm2
        self.pattern_count = pattern_count
        if self.name == None:
            print("Warning: Test not fully defined. Setting non-static.")
            self.static = False
            print("Test has name " + self.name + ".")
        return

    # ===== Get/Set Functions =====

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.name = value
            return 0

    def get_static(self) -> bool:
        return self.static
        
    def set_static(self) -> int:
        self.static = True
        return 0
    
    def get_test_self(self) -> bool:
        return self.test_self

    def set_test_self(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.test_self = value
            return 0

    def get_test_assembly(self) -> bool:
        return self.test_assembly

    def set_test_assembly(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.test_assembly = value
            return 0
    
    def get_defect_coverage(self) -> bool:
        return self.defect_coverage

    def set_defect_coverage(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.defect_coverage = value
            return 0
        
    def get_test_cost_per_mm2(self) -> bool:
        return self.test_cost_per_mm2

    def set_test_cost_per_mm2(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.test_cost_per_mm2 = value
            return 0

    def get_test_quality_param(self) -> bool:
        return self.test_quality_param

    def set_test_quality_param(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.test_quality_param = value
            return 0

    def get_die_numbers(self) -> bool:
        return self.die_numbers

    def set_die_numbers(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static testing.")
            return 1
        else:
            self.die_numbers = value
            return 0
    # ===== End of Get/Set Functions =====

    # ===== Print Functions =====

    def print_description(self) -> None:
        print("Test: " + self.name)
        print("Test_self: " + self.test_self)
        print("Test_assembly: " + self.test_assembly)
        print("Defect_coverage: " + self.defect_coverage)
        print("Test_cost: " + self.test_cost)
        print("Die_numbers: " + self.die_numbers)
        print("Static: " + str(self.static))
        return

    # ===== End of Print Functions =====

    # ===== Other Functions =====
    def computeTestYield(self, chips) -> float:
        if(len(chips) == 0):
            print("Error: Trying to compute quality with no chips in chip list")
            test_yield = 1.0 
            return test_yield
        for chip in chips:
            true_yield = chip.get_wafer_process_yield()
            test_yield = 1-(1-true_yield)*float(self.defect_coverage)
        return test_yield
    
    def computeQuality(self, chips) -> float:
        return 1.0
#        if(len(chips)  == 0):
#            print("Error: Trying to compute quality with no chips in chip list")
#            quality = 1.0   # Compute this chip's quality based on the test.
#            return quality
#        for chip in chips:
#            # pdb.set_trace()
#            true_yield = chip.get_wafer_process_yield()
#            test_yield = 1-(1-true_yield)*float(self.defect_coverage)
#            quality = true_yield/test_yield
#        return quality
    
    def computeTestCost(self, chips) -> float:
        if(len(chips)  == 0):
            print("Error: Trying to compute quality with no chips in chip list")
            TestCost = 1.0   # Compute this chip's quality based on the test.
            return TestCost
        for chip in chips:
            TestCost = chips.get_coreArea()*self.test_cost_per_mm2 #Will need to add pattern count in test def.xml, and chain length parameters in sip.xml
        return TestCost


    # ===== End of Other Functions =====

# =========================================
# Chip Class
# =========================================
# The class has attributes:
#   name: The name of the chip.
#   coreArea: The area of the core in mm^2.
#   cost: The cost of the chip in dollars.
#   chip_yield: The yield of the chip.
#   quality: The quality of the chip.
#   assemblyProcess: The assembly process used to assemble the chip.
#   stackup: The stackup of the chip.
#   chips: The list of chips that are stacked in this chip.
#   adjacencyMatrixList: The list of adjacency matrices for the chip.
#   power: The power of the chip in Watts.
#   static: A boolean set true when the chip is defined to prevent further changes.
# =========================================
# The class has the following methods.
# == Get/Set ==
#   get_name()
#   set_name(string)
#   get_coreArea()
#   set_coreArea(float)
#   get_cost()
#   set_cost(float)
#   get_chip_yield()
#   set_chip_yield(float)
#   get_quality()
#   set_quality(float)
#   get_assemblyProcess()
#   set_assemblyProcess(Assembly)
#   get_stackup()
#   set_stackup(list)
#   get_chips()
#   set_chips(list)
#   get_adjacencyMatrixList()
#   set_adjacencyMatrixList(list)
#   get_power()
#   set_power(float)
#   get_static()
#   set_static()
# == Print ==
#   print_description(): Dumps values of all the parameters for inspection.
# == Other ==
#   computeArea(): Computes the area of the chip in mm^2.
#   computeCost(): Computes the cost of the chip in dollars.
#   computeChipYield(): Computes the yield of the chip.
# =========================================

class Chip:

    # ===== Initialization Functions =====

    def __init__(self, filename="", dict = {}, waferProcessList=[], assemblyProcessList=[], testProcessList=[], layers=[], ios=[], adjacency_matrix_definitions={}, block_names=[], static=False) -> None:
        root = {}
        if filename != "" and dict == {}:
            tree = ET.parse(filename)
            root = tree.getroot()
        elif filename == "" and dict != {}:
            root = dict
        else:
            print("Error: Invalid Chip definition. Must either provide a valid filename or a valid dictionary definition.")
            return

        attributes = root.attrib

        self.chips = []
        for chip_def in root:
            if "chip" in chip_def.tag:
                self.chips.append(Chip(filename="", dict=chip_def, waferProcessList=waferProcessList, assemblyProcessList=assemblyProcessList, testProcessList=testProcessList, layers=layers, ios=ios, adjacency_matrix_definitions=adjacency_matrix_definitions, block_names=block_names, static=static))

        self.name = attributes["name"]                                    # Given Parameter
        self.coreArea = float(attributes["coreArea"])                     # Given Parameter
        if attributes["buried"] == "True":
            self.buried = True                          # Given Parameter
        elif attributes["buried"] == "False":
            self.buried = False
        else:
            print("Error: Invalid buried parameter. Exiting...")
            sys.exit(1)
        # print("Buried = " + str(self.buried) + ".")

        self.waferProcess = self.getWaferProcess(attributes["wafer_process"], waferProcessList)

        self.assemblyProcess = self.getAssemblyProcess(attributes["assembly_process"], assemblyProcessList)

        self.testProcess = self.getTestProcess(attributes["test_process"], testProcessList)
         
        self.stackup = self.buildStackup(attributes["stackup"], layers)                    # Given Parameter

        self.nre_design_cost = float(attributes["nre_design_cost"])        # Given Parameter
        self.quantity = int(attributes["quantity"])                       # Given Parameter

        self.power = float(attributes["power"])                                  # Given Parameter
        self.core_voltage = float(attributes["core_voltage"])                    # Given Parameter
        self.static = static 
         
        if self.name == "" or self.assemblyProcess == "" or self.stackup == [] or ios == [] or adjacency_matrix_definitions == {}:
            print("Error: Chip not fully defined.")
            print("Chip " + self.name + " has parameters coreArea = " + str(self.coreArea) + ", cost = " + str(self.cost) + ", chip_yield = " + str(self.chip_yield) + ", quality = " + str(self.quality) + ", assemblyProcess = " + str(self.assemblyProcess) + ", stackup = " + str(self.stackup) + ", chips = " + str(self.chips) + ", power = " + str(self.power) + ".")
            sys.exit(1)

        # If core area is not given, this is an interposer and only has interconnect, so size is determined from the size of the stacked chiplets.
        self.coreArea = float(attributes["coreArea"])                            # Given Parameter
        # If core area is given, it is possible that the area will be determined by the size of the stacked chiplets or of the IO pads.

        self.stack_power = self.computeStackPower()          # Computed Parameter

        # Compute all computed parameters.
        #self.adjacencyMatrixList = self.buildAdjacencyMatrices(adjacency_matrix_definitions, ios)   # Definitions Given for this Parameter, Needs to be Constructed
        self.globalAdjacencyMatrix = adjacency_matrix_definitions
        self.blockNames = block_names
        self.io_list = ios

        self.quality = self.testProcess.computeQuality(self.chips)            # Computed or Given Parameter

        self.area = self.computeArea()                                      # Computed Parameter Stored to Save Compute Time
        self.cost = self.computeCost()                      # Computed Parameter
        self.chip_yield = self.computeChipYield()           # Computed Parameter

        return

    def computeStackPower(self) -> float:
        stack_power = 0.0
        for chip in self.chips:
            stack_power += chip.get_stack_power()
            stack_power += chip.get_power()
        return stack_power

#    def buildAdjacencyMatrices(self, adjacency_matrix_definitions, ios):
#        
#        # TODO: Implement Here
#
#        adjacencyMatrixList = {}
#        return adjacencyMatrixList

    def getWaferProcess(self, waferProcessName, waferProcessList):
        waferProcess = None
        for wp in waferProcessList:
            if wp.get_name() == waferProcessName:
                waferProcess = wp
                break
        if waferProcess == None:
            print("Error: Wafer Process " + waferProcessName + " not found.")
            sys.exit(1)
        return waferProcess

    def getAssemblyProcess(self, assemblyProcessName, assemblyProcessList):
        assemblyProcess = None
        for ap in assemblyProcessList:
            if ap.get_name() == assemblyProcessName:
                assemblyProcess = ap
                break
        if assemblyProcess == None:
            print("Error: Assembly Process " + assemblyProcessName + " not found.")
            sys.exit(1)
        return assemblyProcess

    def getTestProcess(self, testProcessName, testProcessList):
        testProcess = None
        for tp in testProcessList:
            if tp.get_name() == testProcessName:
                testProcess = tp
                break
        if testProcess == None:
            print("Error: Test Process " + testProcessName + " not found.")
            sys.exit(1)
        return testProcess

    def buildStackup(self, stackup_string, layers):
        stackup = []
        # Split the stackup string at the commas.
        stackup_string = stackup_string.split(",")
        stackup_names = []
        for layer in stackup_string:
            layer_specification = layer.split(":")
            if int(layer_specification[0]) >= 0:
                for i in range(int(layer_specification[0])):
                    stackup_names.append(layer_specification[1])
            else:
                print("Error: Number of layers " + layer_specification[0] + " not valid for " + layer_specification[1] + ".")
                sys.exit(1)
        n_layers = len(stackup_names)
        for layer in stackup_names:
            for l in layers:
                if l.get_name() == layer:
                    stackup.append(l)
                    break
        if len(stackup) != n_layers:
            print("Error: Stackup number of layers does not match definition, make sure all selected layers are included in the layer definition.")
            sys.exit(1)
        return stackup

    # ===== End of Initialization Functions =====

    # ===== Get/Set Functions =====

    def get_name(self) -> str:
        return self.name

    def set_name(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.name = value
            return 0

    def get_coreArea(self) -> float:
        return self.coreArea
    
    def set_coreArea(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.coreArea = value
            return 0

    def get_buried(self) -> bool:
        return self.buried
    
    def set_buried(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.buried = value
            return 0
    
    def get_cost(self) -> float:
        return self.cost
    
    def get_chip_yield(self) -> float:
        return self.chip_yield
    
    def get_quality(self) -> float:
        return self.quality

    def set_quality(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.quality = value
            return 0
    
    def get_assemblyProcess(self):
        return self.assemblyProcess

    def set_assemblyProcess(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.assemblyProcess = value
            return 0
    
    def get_stackup(self) -> list:
        return self.stackup

    def set_stackup(self,layer_list) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.stackup = layer_list
            return 0

    def get_testProcess(self):
        return self.testProcess
    
    def set_testProcess(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.testProcess = value
            return 0
    
    def get_chips_len(self) -> int:
        return len(self.chips)

    def get_chips(self) -> list:
        return self.chips
    
    def set_chip_definitions(self,chip_definitions) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.chips = self.buildChips(chip_definitions)
            return 0
    
#    def get_adjacencyMatrixList(self) -> list:
#        return self.adjacencyMatrixList

    def get_wafer_diameter(self) -> float:
        return self.waferProcess.get_wafer_diameter()
    
    def get_edge_exclusion(self) -> float:
        return self.waferProcess.get_edge_exclusion()
    
    def get_wafer_process_yield(self) -> float:
        return self.waferProcess.get_wafer_process_yield()
    
    def get_reticle_x(self) -> float:
        return self.waferProcess.get_reticle_x()
 
    def get_reticle_y(self) -> float:
        return self.waferProcess.get_reticle_y()
     
    def get_power(self) -> list:
        return self.power

    def set_power(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.power = value
            return 0
    
    def get_core_voltage(self) -> float:
        return self.core_voltage
    
    def set_core_voltage(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.core_voltage = value
            return 0

    def get_stack_power(self) -> list:
        return self.stack_power
    
    def set_stack_power(self) -> int:
        self.stack_power = self.computeStackPower()
        return 0

    def getArea(self) -> float:
        return self.area
    
    def setArea(self) -> int:
        self.area = self.computeArea()
        return 0

    def get_stacked_die_area(self) -> float:
        stacked_die_area = 0.0
        for chip in self.chips:
            if not chip.get_buried():
                stacked_die_area += chip.getArea()
        return stacked_die_area

    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.quantity = value
            return 0

    def get_nre_design_cost(self) -> float:
        return self.nre_design_cost
    
    def set_nre_design_cost(self, value) -> int:
        if (self.static):
            print("Error: Cannot change static chip.")
            return 1
        else:
            self.nre_design_cost = value
            return 0

    def get_static(self) -> bool:
        return self.static
    
    def set_static(self) -> int:
        self.static = True
        return 0

    # ===== End of Get/Set Functions =====

    # ===== Print Functions =====

    def print_description(self):
        print("Chip Name: " + self.name)
        print("Chip Core Area: " + str(self.coreArea))
        print("Area of IO Cells: " + str(self.get_ioArea()))
        print("Number of Chip Power Pads: " + str(self.get_powerPads()))
        print("Number of Signal Pads: " + str(self.get_signal_count(self.get_chip_list())[0]))
        print("Total number of pads: " + str(self.get_powerPads() + self.get_signal_count(self.get_chip_list())[0]))
        print("Area required by pads: " + str(self.get_padArea()))
        print("Chip Calculated Area: " + str(self.area))
        print("Chip Cost: " + str(self.get_cost()))
        print("Self Cost: " + str(self.getLayerAwareCost()))
        print("Chip Yield: " + str(self.get_chip_yield()))
        print("Chip Cost Including Yield: " + str(self.get_cost()/self.get_chip_yield()))
        print("Chip self-yield: " + str(self.computeLayerAwareYield()))
        print("Chip Quality: " + str(self.quality))
        print("Chip Assembly Yield: " + str(self.assemblyProcess.assembly_yield(self.get_chips_len(),self.get_chips_signal_count(),self.get_stacked_die_area())))
        print("Chip Assembly Process: " + self.assemblyProcess.get_name())
        print("Chip Stackup: " + str([l.get_name() for l in self.stackup]))
        print("Chip Test Process: " + self.testProcess.get_name())
        print("Chip Wafer Diameter: " + str(self.get_wafer_diameter()) + "mm")
        print("Reticle Dimensions: (" + str(self.get_reticle_x()) + "," + str(self.get_reticle_y()) + ")mm")
        print("Chip Power: " + str(self.get_power()))
        print("Stack Power: " + str(self.get_stack_power()))
        # print("Chip Adjacency Matrix List: " + str(self.adjacencyMatrixList))
        print("Chip List: " + str([c.get_name() for c in self.chips]))
        #core_area_sum = 0.0
        #io_area_sum = 0.0
        #total_area = 0.0
        #for chip in self.chips:
        #    print("Cost = " + str(chip.get_cost()))
        #    print("Yield = " + str(chip.get_chip_yield()))
        for chip in self.chips:
           print(">>")
           chip.print_description()
        #   core_area_sum += chip.coreArea
        #   total_area += chip.area
        #   io_area_sum += chip.get_ioArea()
        #   if chip.chips != []:
        #       for subchip in chip.chips:
        #            core_area_sum += subchip.coreArea
        #            total_area += subchip.area
        #            io_area_sum += chip.get_ioArea()
           print("<<")
        #core_area_sum += self.coreArea
        #io_area_sum += self.get_ioArea()
        #total_area += self.area
        #print("core_area_sum = " + str(core_area_sum))
        #print("io_area_sum = " + str(io_area_sum))
        #print("total_area = " + str(total_area))
        return


    # ===== End of Print Functions =====

    # ===== Other Functions =====
 
    # Find the total area if a given area is assumed to be square and increased in size by a certain amount in every direction.
    def expandedArea(self,area,border):
        new_area = (math.sqrt(area)+2*border)**2
        return new_area

    # Get the area of the IOs on the chip.
    def get_ioArea(self):
        # TODO: Ultimately, this needs to look at the adjacency matrices and count the number of connections. For now, filler.
        io_area = 0.0
        block_index = None
        for i in range(len(self.blockNames)):
            if self.blockNames[i] == self.get_name():
                block_index = i
                break
        if block_index == None:
            return 0
        for io_type in self.globalAdjacencyMatrix:
            # TODO: Fix this when the adjacency matrix is properly implemented.
            for io in self.io_list:
                if io.get_type() == io_type:
                    break
            # Add all the entries in the row and column of the global adjacency matrix with the index correesponding to the name of the chip and weight with the wire_count of the IO type.
            io_area += sum(self.globalAdjacencyMatrix[io_type][block_index][:]) * io.get_tx_area() + sum(self.globalAdjacencyMatrix[io_type][:][block_index]) * io.get_rx_area()

        return io_area

    # Get the power of the chip and component chips
    def get_power(self):
        return self.power

    # Get number of Power Pads
    def get_powerPads(self):
        power = self.get_power() + self.get_stack_power() + self.get_signal_power(self.get_chip_list())
        power_pads = math.ceil(power / self.assemblyProcess.get_power_per_pad(self.get_core_voltage()))
        power_pads = power_pads*2 # Multiply by 2 for ground and power.
        return power_pads

    # Get the area taken up by the grid of pads on the bottom of the chip at the given pitch.
    def get_padArea(self):
        # TODO: This needs to compute the size of the grid needed for the number of pads. For now, filler.
        num_pads = self.get_powerPads()
        signal_pads, signal_with_reach_count = self.get_signal_count(self.get_chip_list())
        num_pads += signal_pads

        area_per_pad = self.assemblyProcess.get_bonding_pitch()**2

        # Create a list of reaches by taking the keys from the signal_with_reach_count dictionary and converting to floats.
        reaches = [float(key) for key in signal_with_reach_count.keys()]
        # Sort the reaches from smallest to largest.
        reaches.sort()
        current_side = 0.0
        current_count = 0
        for reach in reaches:
            reach_with_separation = reach - self.assemblyProcess.get_die_separation()
            if reach_with_separation < 0:
                print("Error: Reach is smaller than chip separation. Exiting...")
                sys.exit(1)
            current_count += signal_with_reach_count[str(reach)]
            # Find the minimum boundary that would contain all the pads with the current reach.
            required_area = current_count*area_per_pad
            if reach_with_separation < current_side:
                usable_area = reach_with_separation**2 + 2*reach_with_separation*current_side
            else:
                usable_area = current_side**2
            if usable_area <= required_area:
                if math.sqrt(required_area) > reach_with_separation:
                    new_req_side = (required_area - reach_with_separation**2)/(2*reach_with_separation)
                else:
                    new_req_side = math.sqrt(required_area)
                # Round up to the nearest multiple of bonding pitch.
                new_req_side = math.ceil(new_req_side/self.assemblyProcess.get_bonding_pitch())*self.assemblyProcess.get_bonding_pitch()
                if new_req_side > current_side:
                    current_side = new_req_side
        required_area = current_side**2
        grid_side = math.ceil(current_side / self.assemblyProcess.get_bonding_pitch())

        pad_area = grid_side * grid_side * area_per_pad

        return pad_area

    # Get the area of the interposer based on areas of the consituent chiplets.
    # Note that this is an approximation that assumes square chiplets that pack perfectly so it is an optimistic solution that actually gives a lower bound on area.
    # TODO: Implement proper packing and aspect ratio shaping so this is a legitimate solution instead of a strange L shaped interposer for example.
    def computeArea(self):
        # print("Computing area for chip " + self.get_name() + "...")
        chip_io_area = self.get_coreArea() + self.get_ioArea()

        pad_required_area = self.get_padArea()
        
        stacked_die_bound_area = self.get_stacked_die_area()
        #for chip in self.get_chips():
        #    chip_contribution = self.expandedArea(chip.get_coreArea() + chip.get_ioArea(), self.assemblyProcess.get_die_separation()/2)
        #    # print("\tAdding " + str(chip_contribution) + " from chip " + chip.get_name() + " to stacked_die_bound_area.")
        #    stacked_die_bound_area += chip_contribution
        ## print("\tStacked die bound area is " + str(stacked_die_bound_area) + ".")

        # print("Selecting the maximum from: " + str(stacked_die_bound_area) + ", " + str(pad_required_area) + ", and " + str(chip_io_area) + ".")
        # chip_area is the maximum value of the chip_io_area, stacked_die_bound_area, and pad_required_area.
        chip_area = max(stacked_die_bound_area, pad_required_area, chip_io_area)

        return chip_area
 
    def computeNumberReticles(self, area) -> int:
        # TODO: Ground this by actually packing rectangles to calculate a more accurate number of reticles.
        reticle_area = self.get_reticle_x()*self.get_reticle_y()
        num_reticles = math.ceil(area/reticle_area)
        largest_square_side = math.floor(math.sqrt(num_reticles))
        largest_square_num_reticles = largest_square_side**2
        num_stitches = largest_square_side*(largest_square_side-1)*2+2*(num_reticles-largest_square_num_reticles)-math.ceil((num_reticles-largest_square_num_reticles)/largest_square_side)
        return num_reticles, num_stitches
        
    def computeLayerAwareYield(self) -> float:
        layer_yield = 1.0
        for layer in self.stackup:
            layer_yield *= layer.layerYield(self.get_coreArea() + self.get_ioArea())

        return layer_yield

    # Get probability that all component tested chips are good.
    def qualityYield(self) -> float:
        quality_yield = 1.0
        for chip in self.chips:
            quality_yield *= chip.get_testProcess().computeQuality(chip.get_chips())
        return quality_yield

    def get_signal_count(self,internal_block_list):
        # print("Getting signal count")
        # print("Internal block list = " + str(internal_block_list) + ".")
        signal_count = 0
        # This is a dictionary where the key is the reach and the value is the number of signals with that reach.
        signal_with_reach_count = {}

        block_index = None
        internal_block_list_indices = []
        for i in range(len(self.blockNames)):
            if self.blockNames[i] == self.get_name():
                block_index = i
            if self.blockNames[i] in internal_block_list:
                internal_block_list_indices.append(i)
        if block_index == None:
            return 0, {}
        for io_type in self.globalAdjacencyMatrix:
            # TODO: Fix this when the adjacency matrix is properly implemented.
            for io in self.io_list:
                if io.get_type() == io_type:
                    break
            if io.get_bidirectional():
                bidirectional_factor = 0.5
            else:
                bidirectional_factor = 1.0
            # Add all the entries in the row and column of the global adjacency matrix with the index correesponding to the name of the chip and weight with the wire_count of the IO type.
            for j in range(len(self.globalAdjacencyMatrix[io_type][block_index][:])):
                # print("Internal block list indices = " + str(internal_block_list_indices) + ".")
                # print("Adjacency matrix:" + str(self.globalAdjacencyMatrix[io_type][:][:]))
                if j not in internal_block_list_indices:
                    # print("Adding to signal count for " + self.blockNames[j] + ".")
                    # print("io signal width = " + str(io.get_wire_count()) + ".")
                    # print("Signal count before = " + str(signal_count) + ".")
                    signal_count += (self.globalAdjacencyMatrix[io_type][block_index][j] + self.globalAdjacencyMatrix[io_type][j][block_index]) * io.get_wire_count() * bidirectional_factor
                    # print("Signal count after = " + str(signal_count) + ".")
                    if str(io.get_reach()) in signal_with_reach_count:
                        signal_with_reach_count[str(io.get_reach())] += (self.globalAdjacencyMatrix[io_type][block_index][j] + self.globalAdjacencyMatrix[io_type][j][block_index]) * io.get_wire_count() * bidirectional_factor
                    else:
                        signal_with_reach_count[str(io.get_reach())] = (self.globalAdjacencyMatrix[io_type][block_index][j] + self.globalAdjacencyMatrix[io_type][j][block_index]) * io.get_wire_count() * bidirectional_factor
            #signal_count += (sum(self.globalAdjacencyMatrix[io_type][block_index][:]) + sum(self.globalAdjacencyMatrix[io_type][:][block_index])) * io.get_wire_count()
        
        # print("Signal count = " + str(signal_count) + ".")
        # print("Signal with reach count = " + str(signal_with_reach_count) + ".")

        # print()

        return signal_count, signal_with_reach_count

    def get_signal_power(self,internal_block_list) -> float:
        signal_power = 0.0
        block_index = None
        internal_block_list_indices = []
        for i in range(len(self.blockNames)):
            if self.blockNames[i] == self.get_name():
                block_index = i
            if self.blockNames[i] in internal_block_list:
                internal_block_list_indices.append(i)
        if block_index == None:
            return 0
        for io_type in self.globalAdjacencyMatrix:
            # TODO: Fix this when the adjacency matrix is properly implemented.
            for io in self.io_list:
                if io.get_type() == io_type:
                    break
            if io.get_bidirectional():
                bidirectional_factor = 0.5
            else:
                bidirectional_factor = 1.0
            signal_power += (sum(self.globalAdjacencyMatrix[io_type][block_index][:]) + sum(self.globalAdjacencyMatrix[io_type][:][block_index])) * io.get_bandwidth() * io.get_energy_per_bit() * bidirectional_factor
        return signal_power

    def get_chip_list(self):
        chip_list = []
        for chip in self.chips:
            chip_list.append(chip.get_chip_list())
        chip_list.append(self.get_name())
        return chip_list

    def get_chips_signal_count(self) -> int:
        signal_count = 0

        internal_chip_list = self.get_chip_list()

        for chip in self.chips:
            signal_count += chip.get_signal_count(internal_chip_list)[0]
        return signal_count

    def computeChipYield(self) -> float:
        chip_yield = self.computeLayerAwareYield()
        # Account for quality of component chiplets.
        # Account for assembly yield.
        # Account for yield of this chip.
        quality_yield = self.qualityYield()
        # print("\t\tQuality yield is " + str(quality_yield) + ".")
        assembly_yield = self.assemblyProcess.assembly_yield(self.get_chips_len(),self.get_chips_signal_count(),self.get_stacked_die_area())
        # print("\t\tAssembly yield is " + str(assembly_yield) + ".")
        chip_yield *= quality_yield*assembly_yield*self.get_wafer_process_yield()
        self.chip_yield = chip_yield
        # print("\t\tComputed chip yield for " + self.get_name() + " is " + str(chip_yield) + ".")
        return chip_yield

    def wafer_area_eff(self) -> float:
        # TODO: Need to add a function or closed form solution to find the Gauss' circle problem for the number of chips that can fit on a wafer.
        usable_wafer_radius = (self.get_wafer_diameter()/2)-self.get_edge_exclusion()
        usable_wafer_area = math.pi*(usable_wafer_radius)**2
        return usable_wafer_area

    def getLayerAwareCost(self):
        cost = 0
        for layer in self.stackup:
            cost += layer.layerCost(self.area, self.waferProcess)
        return cost

    def getMaskCost(self):
        cost = 0
        for layer in self.stackup:
            cost += layer.get_mask_cost()
        return cost

    def computeCost(self) -> float:
        # print("Computing cost for chip " + self.get_name() + "...")
        cost = self.getLayerAwareCost()
        # Add cost of this chip
        # print("The cost of the self-contained chip is " + str(cost) + ".")
        # Add cost of stacked chips
        for i in range(len(self.chips)):
            cost += self.chips[i].get_cost()/self.chips[i].get_chip_yield()
        # Add assembly cost 
        assembly_cost = self.assemblyProcess.assembly_cost(self.get_chips_len(),self.get_chips_signal_count(),self.get_stacked_die_area())
        # print("Assembly cost = " + str(assembly_cost) + ".")
        cost += assembly_cost
        # TODO: Add test cost 


        # NRE Cost
        nre_cost = (self.get_nre_design_cost() + self.getMaskCost())/self.get_quantity()
        cost += nre_cost

        # Not accounting for yield here. Account for yield later.
        ## Account for yield
        #chip_yield = self.computeChipYield()
        #print("Chip yield = " + str(chip_yield) + ".")

        #cost = cost/chip_yield

        # Store new computed cost
        self.cost = cost
        return cost

    ## Return core area of the chiplet by summing component IP areas without inculding IOs or boundary exclusion zones.
    #def getChipletCoreArea(assignments, nodes, tech_def_array, tech_area_multiplier, chiplet_number):
    #    # assignments - list of partitions which are lists of nodes
    #    # nodes - list of nodes
    #    # tech_def_array - array of tech selection for each chiplet
    #    # tech_area_multiplier - array of area multipliers for each tech
    #    # chiplet_number - the chiplet to get the core area for

    #    chiplet_core_area = 0

    #    for i in range(len(assignments[chiplet_number])):
    #        chiplet_core_area += nodes[assignments[chiplet_number][i]][2]*tech_area_multiplier[tech_def_array[i]]

    #    return chiplet_core_area

    ## Return the count of IOs in the chiplet. Right now this includes total, output, and input.
    ## May need to increase the number of categories or switch to an array of counts along with an array of corresponding IO types.
    #def getChipletIOCount(a, assignments, chiplet_number):
    #    # a - adjacency matrix
    #    # assignments - list of partitions which are lists of nodes
    #    # chiplet_number - the chiplet to get the IO count for

    #    chiplet_num_io = 0
    #    chiplet_num_output = 0
    #    chiplet_num_input = 0

    #    for j in assignments[chiplet_number]:
    #        for l in range(len(assignments)):
    #            if l != chiplet_number:
    #                for k in assignments[l]:
    #                    chiplet_num_output += a[j][k]
    #                    chiplet_num_input += a[k][j]

    #    chiplet_num_io = chiplet_num_output + chiplet_num_input

    #    return chiplet_num_io, chiplet_num_output, chiplet_num_input

    ## Return the area taken by IOs in the chiplet.
    #def getIOArea(chiplet_num_io, chiplet_num_output, chiplet_num_input):
    #    # chiplet_num_io - the number of IOs in the chiplet
    #    # chiplet_num_output - the number of outputs in the chiplet
    #    # chiplet_num_input - the number of inputs in the chiplet

    #    io_area = chiplet_num_io*params.io_size

    #    # TODO: Handle different types of IOs here. Likely will need to add more parameters above. Perhaps a dictionary of IO types and their sizes?

    #    return io_area

    ## Returns the number of connected chiplets for each chiplet to allow optimization for fewer connections.
    ## This is meant to help floorplanning.
    #def getNumConnectedChipletsArray(a, assignments):
    #    # a - adjacency matrix
    #    # assignments - list of partitions which are lists of nodes

    #    chiplet_num_connected_chiplets = []

    #    for i in range(len(assignments)):
    #        chiplet_num_connected_chiplets.append(0)

    #    for i in range(len(assignments)):
    #        for j in range(i,len(assignments)):
    #            connected = 0
    #            for k in assignments[i]:
    #                for l in assignments[j]:
    #                    if a[k][l] > 0 or a[l][k] > 0:
    #                        connected = 1
    #            chiplet_num_connected_chiplets[i] += connected
    #            chiplet_num_connected_chiplets[j] += connected

    #    return chiplet_num_connected_chiplets

    # ===== End of Other Functions =====








# Interconnect Adjacency Matrix Class
# The class has the following attributes (These should be treated as private.):
#   type: The type of IO for this adjacency matrix. (Select from list of IO definitions.)
#   block_names: The names of the blocks in the adjacency matrix.
#   adjacency_matrix: The adjacency matrix itself.
#   static: A boolean value indicating whether the adjacency matrix is static or not. (This is meant to act like a latch.)
# The class has the following methods:
#   get_type(): Returns the type of the adjacency matrix.
#   set_type(): Sets the type of the adjacency matrix.
#   get_block_names_length(): Returns the length of the block names list.
#   get_block_names_entry(index): Returns the block name at the given index.
#   set_block_names_entry(index, value): Sets the block name at the given index to the given value.
#   get_block_names(): Returns the block names of the adjacency matrix.
#   set_block_names(): Sets the block names of the adjacency matrix.
#   get_adjacency_matrix_shape(): Returns the shape of the adjacency matrix.
#   get_adjacency_matrix_entry(row, column): Returns the entry at the given row and column.
#   set_adjacency_matrix_entry(row, column, value): Sets the entry at the given row and column to the given value.
#   get_adjacency_matrix(): Returns the adjacency matrix.
#   set_adjacency_matrix(): Sets the adjacency matrix.
#   get_static(): Returns the static value of the adjacency matrix.
#   set_static(): Sets the static value of the adjacency matrix.

#class InterconnectAdjacencyMatrix:
#    def __init__(self, type=None, IO_list=None, block_names=None, adjacency_matrix=[], static=False) -> None:
#        self.type = type
#        self.block_names = block_names
#        self.adjacency_matrix = adjacency_matrix
#        self.static = static
#        if self.type == None:
#            print("Error: Type not defined for Interconnect Adjacency Matrix. Exiting...")
#            sys.exit(1) 
#        # If the adjacency matrix is empty, exit.
#        if self.adjacency_matrix == []:
#            print("Error: Adjacency matrix not defined for Interconnect Adjacency Matrix. Exiting...")
#            sys.exit(1)
#        # If the adjacency matrix is not square, exit.
#        if len(self.adjacency_matrix) != len(self.adjacency_matrix[0]) or len(self.adjacency_matrix.shape) != 2:
#            print("Error: Adjacency matrix is not square. Exiting...")
#            sys.exit(1)
#        if self.block_names == None:
#            print("Warning: Block names not defined for Interconnect Adjacency Matrix. Generating default block names.")
#            block_names = []
#            for i in range(len(self.adjacency_matrix)):
#                block_names.append("Block " + str(i))
#        # If block_names is not the same length as the side of adjacency matrix exit.
#        if len(self.block_names) != len(self.adjacency_matrix):
#            print("Error: Block names is not the same length as the side of the adjacency matrix. Exiting...")
#            sys.exit(1)
#        if IO_list == None:
#            print("Error: IO list not defined for Interconnect Adjacency Matrix. Exiting...")
#            sys.exit(1)
#        self.IO = None
#        for IO in IO_list:
#            if IO.get_type() == type:
#                self.IO = IO
#                break
#        if self.IO == None:
#            print("Error: No IO of type " + type + " found.")
#            print("Exiting...")
#            sys.exit(1)
#        return
#
#    # ===== Get/Set Functions =====
#
#    def get_type(self) -> str:
#        return self.type
#
#    def get_block_names_len(self) -> int:
#        return len(self.block_names)
#
#    def get_block_names_entry(self, index) -> str:
#        return self.block_names[index]
#
#    def set_block_names_entry(self, index, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static IO.")
#            return 1
#        else:
#            self.block_names[index] = value
#            return 0    
#
#    def get_block_names(self) -> list:
#        return self.block_names
#
#    def set_block_names(self, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static IO.")
#            return 1
#        else:
#            self.block_names = value
#            return 0
#
#    def get_adjacency_matrix_shape(self) -> tuple:
#        return self.adjacency_matrix.shape
#
#    def get_adjacency_matrix_entry(self, TX, RX) -> int:
#        return self.adjacency_matrix[TX][RX]
#    
#    def set_adjacency_matrix_entry(self, TX, RX, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static IO.")
#            return 1
#        else:
#            self.adjacency_matrix[TX][RX] = value
#            return 0
#
#    def get_adjacency_matrix(self) -> np.ndarray:
#        return self.adjacency_matrix
#
#    def set_adjacency_matrix(self, value) -> int:
#        if (self.static):
#            print("Error: Cannot change static IO.")
#            return 1
#        else:
#            self.adjacency_matrix = value
#            return 0
#
#    def get_static(self) -> bool:
#        return self.static
#    
#    def set_static(self) -> int:
#        self.static = True
#        return 0
#
#    # ===== End of Get/Set Functions =====
#
#    # ===== Print Functions =====
#
#    def print_description(self) -> None:
#        print("Type: " + self.type)
#        print("Static: " + str(self.static))
#
#        print("\t\t",end="")   
#        for i in range(len(self.block_names)):
#            print(self.block_names[i],end="\t")
#        print()
#        for i in range(len(self.block_names)):
#            print(self.block_names[i],end="\t")
#            for j in range(len(self.block_names)):
#                print(self.adjacency_matrix[i][j],end="\t")
#        return
#
#    # ===== End of Print Functions =====
#
#    # ===== Other Functions =====
#
#    def combine_blocks(self, block_1, block_2) -> int:
#        if (self.static):
#            print("Error: Cannot change static IO.")
#            return 1
#        else:
#            if block_1 == block_2:
#                print("Error: Cannot combine a block with itself.")
#                return 1
#            self.block_names[block_1] = self.block_names[block_1] + "," + self.block_names[block_2]
#            self.block_names.pop(block_2)
#            shape_am = self.adjacency_matrix.shape
#            for i in range(shape_am[0]):
#                if i != block_1 and i != block_2:
#                    self.adjacency_matrix[i][block_1] = self.adjacency_matrix[i][block_1] + self.adjacency_matrix[i][block_2]
#                    self.adjacency_matrix[i][block_2] = 0
#            for i in range(shape_am[1]):
#                if i != block_1 and i != block_2:
#                    self.adjacency_matrix[block_1][i] = self.adjacency_matrix[block_1][i] + self.adjacency_matrix[block_2][i]
#                    self.adjacency_matrix[block_2][i] = 0
#            self.adjacency_matrix = np.delete(self.adjacency_matrix, block_2, 0)
#            self.adjacency_matrix = np.delete(self.adjacency_matrix, block_2, 1)
#            return 0  
#
#    # ===== End of Other Functions =====