# =========================================================================
# = This file contains the functions to read the given library xml files. =
# =========================================================================

import design as d
import numpy as np
import xml.etree.ElementTree as ET
import math
import sys

# Function to read the wafer process definitions.
def waferProcessDefinitionListFromFile(filename):
    # print("Reading wafer process definitions from file: " + filename)
    # Read the XML file.
    tree = ET.parse(filename)
    # Get root of the XML file.
    root = tree.getroot()
    # List of wafer process .
    wp_list = []
    # Iterate over the IO definitions.
    for wp_def in root:
        # Create an Wafer Process object.
        wp = d.WaferProcess("",0.0,0.0,0.0,0.0,0.0,0.0,False)
        attributes = wp_def.attrib
        # Iterate over the IO definition attributes.
        # Set the IO object attributes.
        wp.set_name(attributes["name"])
        wp.set_wafer_diameter(float(attributes["wafer_diameter"]))
        wp.set_edge_exclusion(float(attributes["edge_exclusion"]))
        wp.set_wafer_process_yield(float(attributes["wafer_process_yield"]))
        wp.set_dicing_distance(float(attributes["dicing_distance"]))
        wp.set_reticle_x(float(attributes["reticle_x"]))
        wp.set_reticle_y(float(attributes["reticle_y"]))
        wp.set_static()
        # Append the IO object to the list.
        wp_list.append(wp)
    # Return the list of wafer process definition objects.
    return wp_list

# Define a function to read the IO definitions from a file.
def ioDefinitionListFromFile(filename):
    # print("Reading IO definitions from file: " + filename)
    # Read the XML file.
    tree = ET.parse(filename)
    root = tree.getroot()
    # Create a list of IO objects.
    io_list = []
    # Iterate over the IO definitions.
    for io_def in root:
        # Create an IO object.
        io = d.IO("",0.0,0.0,0.0,0.0,0,False,0.0,0.0,False)
        attributes = io_def.attrib
        # Iterate over the IO definition attributes.
        # Set the IO object attributes.
        io.set_type(attributes["type"])
        io.set_rx_area(float(attributes["rx_area"]))
        io.set_tx_area(float(attributes["tx_area"]))
        io.set_shoreline(float(attributes["shoreline"]))
        io.set_bandwidth(float(attributes["bandwidth"]))
        io.set_wire_count(int(attributes["wire_count"]))
        io.set_bidirectional(bool(attributes["bidirectional"]))
        io.set_energy_per_bit(float(attributes["energy_per_bit"]))
        io.set_reach(float(attributes["reach"]))
        io.set_static()
        # Append the IO object to the list.
        io_list.append(io)
    # Return the list of IO objects.
    return io_list

# Define a function to read the layer definitions from a file.
def layerDefinitionListFromFile(filename):
    # print("Reading layer definitions from file: " + filename)
    # Read the XML file.
    tree = ET.parse(filename)
    root = tree.getroot()
    # Create a list of layer objects.
    layer_list = []
    # Iterate over the layer definitions.
    for layer_def in root:
        # Create a layer object.
        layer = d.Layer("",False,0,0,0,0,0,0,0,False)
        attributes = layer_def.attrib
        # Set the layer object attributes.
        layer.set_name(attributes["name"])
        layer.set_active(bool(attributes["active"]))
        layer.set_cost_per_mm2(float(attributes["cost_per_mm2"]))
        layer.set_defect_density(float(attributes["defect_density"]))
        layer.set_critical_area_ratio(float(attributes["critical_area_ratio"]))
        layer.set_clustering_factor(float(attributes["clustering_factor"]))
        layer.set_litho_percent(float(attributes["litho_percent"]))
        layer.set_mask_cost(float(attributes["nre_mask_cost"]))
        layer.set_stitching_yield(float(attributes["stitching_yield"]))

        layer.set_static()
        # Append the layer object to the list.
        layer_list.append(layer)
    # Return the list of layer objects.
    return layer_list

# Define a function to read the assembly process definitions from a file.
def assemblyProcessDefinitionListFromFile(filename):
    # print("Reading assembly process definitions from file: " + filename)
    # Read the XML file.
    tree = ET.parse(filename)
    root = tree.getroot()
    # Create a list of assembly process objects.
    assembly_process_list = []
    # Iterate over the assembly process definitions.
    for assembly_process_def in root:
        # Create an assembly process object.
        assembly_process = d.Assembly("",0.0,"",0.0,0.0,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,0.0,0,0.0,0.0,0.0,0.0,False)
        
        attributes = assembly_process_def.attrib

        assembly_process.set_name(attributes["name"])
#        # The following would set machine and technician parameters as a list of an undefined length.
#        # This has been switched to defining these parameters in terms of two values, one for bonding and one for pick and place.
#        # Leaving this for now, in case a reason comes up to rever to the old version.
#        assembly_process.set_machine_cost_list([float(x) for x in attributes["machine_cost_list"].split(',')])
#        assembly_process.set_machine_lifetime_list([float(x) for x in attributes["machine_lifetime_list"].split(',')])
#        assembly_process.set_machine_uptime_list([float(x) for x in attributes["machine_uptime_list"].split(',')])
#        assembly_process.set_technician_yearly_cost_list([float(x) for x in attributes["technician_yearly_cost_list"].split(',')])
        assembly_process.set_materials_cost_per_mm2(float(attributes["materials_cost_per_mm2"]))
        assembly_process.set_assembly_type(attributes["assembly_type"])
        assembly_process.set_picknplace_machine_cost(float(attributes["picknplace_machine_cost"]))
        assembly_process.set_picknplace_machine_lifetime(float(attributes["picknplace_machine_lifetime"]))
        assembly_process.set_picknplace_machine_uptime(float(attributes["picknplace_machine_uptime"]))
        assembly_process.set_picknplace_technician_yearly_cost(float(attributes["picknplace_technician_yearly_cost"]))
        assembly_process.set_picknplace_time(float(attributes["picknplace_time"]))
        assembly_process.set_picknplace_group(int(attributes["picknplace_group"]))
        assembly_process.set_bonding_machine_cost(float(attributes["bonding_machine_cost"]))
        assembly_process.set_bonding_machine_lifetime(float(attributes["bonding_machine_lifetime"]))
        assembly_process.set_bonding_machine_uptime(float(attributes["bonding_machine_uptime"]))
        assembly_process.set_bonding_technician_yearly_cost(float(attributes["bonding_technician_yearly_cost"]))
        assembly_process.set_bonding_time(float(attributes["bonding_time"]))
        assembly_process.set_bonding_group(int(attributes["bonding_group"]))
        assembly_process.compute_picknplace_cost_per_second()
        assembly_process.compute_bonding_cost_per_second()
        assembly_process.set_die_separation(float(attributes["die_separation"]))
        assembly_process.set_edge_exclusion(float(attributes["edge_exclusion"]))
        assembly_process.set_bonding_pitch(float(attributes["bonding_pitch"]))
        assembly_process.set_max_pad_current_density(float(attributes["max_pad_current_density"]))
        assembly_process.set_alignment_yield(float(attributes["alignment_yield"]))
        assembly_process.set_bonding_yield(float(attributes["bonding_yield"]))
        assembly_process.set_dielectric_bond_defect_density(float(attributes["dielectric_bond_defect_density"]))

        assembly_process.set_static()     

        # Append the assembly process object to the list.
        assembly_process_list.append(assembly_process)
    # Return the list of assembly process objects.
    return assembly_process_list

# Define a function to read the test process definitions from a file.
def testProcessDefinitionListFromFile(filename):
    # print("Reading test process definitions from file: " + filename)
    # Read the XML file.
    tree = ET.parse(filename)
    root = tree.getroot()
    # Create a list of test process objects.
    test_process_list = []
    # Iterate over the test process definitions.
    for test_process_def in root:
        # Create a test process object.
        test_process = d.Test("",False,False,0.0,0.0,0,0.0,0,False)

        attributes = test_process_def.attrib
        test_process.set_name(attributes["name"])
        test_process.set_static()

        test_process_list.append(test_process)
    
    return test_process_list

# Define a function to construct the global adjacency matrix from the netlist file.
def globalAdjacencyMatrixFromFile(filename, io_list):
    # print("Reading netlist from file: " + filename)
    # Read the XML file.
    tree = ET.parse(filename)
    root = tree.getroot()

    # Split the root.attrib["block_names"] string at commas and store in list.
    block_names = [] 

    # The output format is a dictionary of items with format {type: numpy array adjacencey matrix}
    global_adjacency_matrix = {}

    # Iterate over the net definitions.
    for net_def in root:
        # Check if the type of net is already a key in the dictionary.
        if net_def.attrib["type"] not in global_adjacency_matrix:
            # print("Adding new net type to adjacency matrix: " + net_def.attrib["type"])
            # If so, append the new net to the existing adjacency matrix.
            global_adjacency_matrix[net_def.attrib["type"]] = np.zeros((len(block_names),len(block_names)))

        # If block 1 or block 2 is not in the list of block names, add it.
        if net_def.attrib["block0"] not in block_names:
            # print("Adding new block to adjacency matrix: " + net_def.attrib["block0"])
            block_names.append(net_def.attrib["block0"])
            # Add a row and column to each numpy adjacency matrix.
            for key in global_adjacency_matrix:
                global_adjacency_matrix[key] = np.pad(global_adjacency_matrix[key],((0,1),(0,1)),'constant',constant_values=0)
        if net_def.attrib["block1"] not in block_names:
            # print("Adding new block to adjacency matrix: " + net_def.attrib["block1"])
            block_names.append(net_def.attrib["block1"])
            # Add a row and column to each numpy adjacency matrix.
            for key in global_adjacency_matrix:
                global_adjacency_matrix[key] = np.pad(global_adjacency_matrix[key],((0,1),(0,1)),'constant',constant_values=0)

        io_bandwidth = None
        bidirectional = None   
        
        # print("Searching for and IO type that matches " + net_def.attrib["type"])
        for io in io_list:
            #print(io.get_type())
            if net_def.attrib["type"] == io.get_type():
                io_bandwidth = io.get_bandwidth()
                bidirectional = io.get_bidirectional()

        if io_bandwidth == None or bidirectional == None:
            print("ERROR: Net type " + net_def.attrib["type"] + " not found in io_list.")
            sys.exit(1)

        # Find the indices of the two blocks connected by the net.
        block1_index = block_names.index(net_def.attrib["block0"])
        block2_index = block_names.index(net_def.attrib["block1"])
        if not bidirectional:
            global_adjacency_matrix[net_def.attrib["type"]][block1_index,block2_index] += int(math.ceil(float(net_def.attrib["bandwidth"])/io_bandwidth))
        else:
            global_adjacency_matrix[net_def.attrib["type"]][block1_index,block2_index] += int(math.ceil(float(net_def.attrib["bandwidth"])/io_bandwidth))
            global_adjacency_matrix[net_def.attrib["type"]][block2_index,block1_index] += int(math.ceil(float(net_def.attrib["bandwidth"])/io_bandwidth))

    return global_adjacency_matrix, block_names

# Define a function to construct the root chip and all subchips from a definition file.
def chipFromDict(dict, io_list, layer_list, wafer_process_list, assembly_process_list, test_process_list, global_adjacency_matrix, block_names):
    # print("Reading chip definition from dictionary...")
    # attributes = dict.attrib

    # chips = []
    # # For each chip within the chip, create a new chip and append to a list.
    # for chip_def in dict:
    #     if chip_def.tag == "chip":
    #         chips.append(chipFromDict(chip_def, io_list, layer_list, wafer_process_list, assembly_process_list, test_process_list, global_adjacency_matrix, block_names))

    chip = d.Chip(filename="",dict=dict,waferProcessList=wafer_process_list,assemblyProcessList=assembly_process_list,testProcessList=test_process_list,layers=layer_list,ios=io_list,adjacency_matrix_definitions=global_adjacency_matrix,block_names=block_names,static=False)
    #chip = d.Chip(attributes["name"], float(attributes["coreArea"]), wafer_process_list, assembly_process_list, attributes["assembly_process"], layer_list, attributes["stackup"], test_process_list, attributes["test_process"], global_adjacency_matrix, block_names, chips=chips, ios=io_list, powerPins=int(attributes["powerPins"]), groundPins=int(attributes["groundPins"]))
    return chip

# def rootChipFromFile(filename,io_list,layer_list,wafer_process_list,assembly_process_list,test_process_list,global_adjacency_matrix,block_names):
#     print("Reading root chip definition from file: " + filename)
#     # Read the XML file.
#     tree = ET.parse(filename)
#     root = tree.getroot()
#     # Create a root chip object.
#     root_chip = d.Chip("",root,io_list,layer_list,wafer_process_list,assembly_process_list,test_process_list,global_adjacency_matrix,block_names)
#     #root_chip = chipFromDict(root,io_list,layer_list,wafer_process_list,assembly_process_list,test_process_list,global_adjacency_matrix,block_names)

    
#     return root_chip

