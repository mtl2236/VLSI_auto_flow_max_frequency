import sys
import os
import string
import math
#running Genus synthesis,transform Design name into Genus run.tcl 
os.system("./Genus_run.sh %s" %(sys.argv[1]))
#runing a shell script,finding the last line in genus log containing Total cell area information
res=os.popen("./Finding_total_cell_area.sh")
line=res.readlines()
#List transform to string
s='\n'.join(line)
#delete '\n'
s=s.strip()
#delete ','
s=s.replace(',','')
#transform string to float
Total_cell_area=float(s)
#assume die is squart, area is four times of total cell area
Die_Size=1.8*Total_cell_area
#get the squart length
length=int(math.sqrt(Die_Size)+5)
length=str(length)
#print length
#create a file to save length
f=open('output_par.txt','w')
f.write(length)
f.close()
