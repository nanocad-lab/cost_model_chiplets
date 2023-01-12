# chiplet_cost_model
Analytical model of cost of chipletization for different chiplet sizes.

# Link to Paper
The paper is published xxxx in xxxx and may be found at xxxx.

# Usage Instructions
For basic usage run "python main.py" from the main directory. Parameters defining the system in question are in system.xml and the parameters defining specific technologies are located in tech.xml. chiplet_cost_calculator.py contains the cost model functions. Read the comments in .py and .xml files for further information.

# Notes on Outstanding TODOs
 - The second half of the main.py file is commented out. Originally, this was intended to replicate the sweeps we used to generate figures in our paper submission, but after overhauling the interface to use XML files as input, this part of main.py is no longer compatible.
 - IO cells are not handled properly for area and power impacts. Excel version used a lookup table based on SPICE results, but it would be nicer to integrate with spice or have a formula for the Python model.
 - Performance aware yield is not included.
 - constants.py was used for the previous interface, but is not currently used. After a reimplementation of the sweep with the new interface, the constants file will be removed.
