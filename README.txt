====================================
README for Chiplet Cost Model
====================================

General Usage:
python load_and_test_design.py io_definitions.xml layer_definitions.xml wafer_process_definitions.xml assembly_process_definitions.xml test_definitions.xml netlist.xml sip.xml

The above command will run the cost calculation on the demo configuration file sip.xml and demo netlist file netlist.xml

Requirements:
Currently, I am running this using:
    Python 3.10.6
    Numpy 1.25.0
    xml.etree.ElementTree 1.3.0


====================================
Included Files:
====================================

design.py
    Contains class definitions for the chip class that is core to the model along with class definitions for layers, IOs, testing processes, wafer processes, and assembly methods.

generate_test_files.py
    This is used to generate the netlist and system definition files for the 800mm^2 testcase.

load_and_test_design.py
    This is used to pass file names as an argument and build the system. This also prints out the computed system information.

readDesignFromFile.py
    Functions for reading xml files into the dictionary format and processing into the class structure are included here.

sip.xml
    Demo system definition file

netlist.xml
    Demo netlist file

io_definitions.xml
    IO definitions file

layer_definitions.xml
    Layer definition file. This contains both "combined" layers that model a full stackup and individual layers such as metal and active layers to build a full stackup based on number of required metal layers.

test_definitions.xml
    Test process definition file. This contains the constants necessary to compute testing cost and to compute a testing method aware yield.

wafer_process_definitions.xml
    This contains the constants that are generally shared about parameters such as reticle size and wafer processing yield.

assembly_process_definitions.xml
    This contains definitions of constants necessary for computing the assembly cost and yield impact.


====================================
General Summary
====================================

The general organization of the code:
 - Class definitions and model functions are included in design.py
 - Functions for reading the design are included in readDesignFromFile.py
 - load_and_test_design.py is a wrapper that makes this easier to use to test a single design.

Modify or create new .xml files to evaluate new systems and processes. To add new considerations, edit the corresponding class in design.py.
