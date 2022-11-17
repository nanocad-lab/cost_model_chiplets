import math

# Constants

# Bonding and Placement
# Simultaneous Bonding means chiplets are placed separately, but bonded at the same time as with solder reflow.
# Individual Bonding means chiplets are bonded individually as they are placed.
simultaneous_bonding = True
# Some machines have multiple placement heads. Indicate the number of chiplets placed at a time here.
place_group_size = 1
# Placement time (s)
tplace = 10
# Bonding time (s) This will vary depending on the type of bond.
tbond = 20

# Machine Costs
# Yearly Personel Cost (USD)
labor_cost = 200000
# Upfront Machine Cost (USD)
#machine_cost = 1000000
machine_cost = 200000
# Useful Time of Machine (years)
machine_depreciation_time = 5
# This is the assembly cost per second.
assembly_cost_per_s = (labor_cost+machine_cost/machine_depreciation_time)/(356*24*60*60)

# Reticle Size (mm)
reticle_xdim = 26
reticle_ydim = 33
reticle_area = reticle_xdim*reticle_ydim

# Wafer Size (mm)
wafer_diameter = 300
edge_exclusion = 3
wafer_area = math.pi*((wafer_diameter/2)-edge_exclusion)**2

# Estimated Full Wafer Costs for a 300mm wafer (USD)
# TODO: Add switch for wafer size and technology node.
interposer_wafer_cost = 1487.08
wafer_40nm_cost = 3200.00
blank_wafer_cost = 500.00
interposer_wafer_cost_per_mm2 = interposer_wafer_cost/wafer_area
wafer_cost_per_mm2 = wafer_40nm_cost/wafer_area
blank_wafer_cost_per_mm2 = blank_wafer_cost/wafer_area

# Yield Parameters
# Defect Density (/mm^2)
defect_density = 0.004
# Clustering Factor
clustering_factor = 2
# Alignment Yield
yield_alignment = 0.999

# Delay and Power Parameters
# Capacitance per um^2 (pF)
wire_cap = 0.0000613889
# Wire Width (um)
wire_width = 0.4

# Chiplet Separation on Interposer (um)
chiplet_separation = 300

# Rent's Rule Constants
# Microprocessor
a = 0.45
k = 0.82
## Random Logic
#a = 0.63
#k = 1.4

# ESD Area Calculations (um^2)
# Area of a single diode used in SPICE model.
diode_area = 3.7556
diode_pair_area = diode_area*2
IO_buffer_size = 47.63
# Clock Rate (Hz)
clk_rate = 1000000000
activity_factor = 0.5
vdd = 1.1

# ESD Parameters from SPICE
# (V)
esd_cdm_levels  = {0,  10,  125,  250,  500}
esd_diode_pairs = {0,   2,    6,   11,   20}
# (fF)
esd_cap         = {0,8.02,18.97,37.65,74.97}

# Average Gate Size (mm^2)
average_gate_size = 0.0000010584
