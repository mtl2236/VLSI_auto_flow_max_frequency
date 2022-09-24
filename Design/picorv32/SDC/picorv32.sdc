set sdc_version 1.4


# Set the current design
current_design picorv32

set_units -time 1ns
set_units -capacitance 1pF

#set_case_analysis 0 [get_ports test_mode]
#set_case_analysis 0 [get_ports scan_en]
create_clock -name "CLK" -add -period 5.0  [get_ports clk]

#set_false_path -from [list \
#  [get_ports reset]  \
#  [get_ports test_mode] ]

#set_false_path -hold -through [get_pins PM_INST/clk_enable]


#set_max_fanout 15.000 [current_design]
#set_max_transition 1.2 [current_design]
