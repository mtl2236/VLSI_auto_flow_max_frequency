#!/bin/bash
#Finding the last line containing"Total cell Area:"
#Total Cell Area:              653,636         728,000         812,000         812,000
area_line=$(sed -n '/Total Cell Area:/p' logs/base.log |tail -n1)
#Split the line into an array of strings 
a=($area_line)
#Getting the length of the array 
num=${#a[@]}
#returning the last string to Python script
echo ${a[$num-1]}
