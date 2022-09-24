import sys
import os
import string
import math
import shutil
import os.path

multi_par=10
threshold=5


#judge the log of Innovus under the frenquency "f" and determin fmin and fmax
def judge_innovus_log(string):
    f=open(string+'/base.log','r+')
    flist=f.readlines()
    for i in range(len(flist)):
        if "No constrained timing paths with given description found." in flist[i]:   #no setup violation has been found, this frequency pass
            f.close()
            return 'pass'  
    f.close()
    return 'Fail'
    
#main 
f=open('iteration.txt','r+')
flist=f.readlines()
rerun=(flist[0].split())[-1]
iteration_times=(flist[1].split())[-1]
f=(flist[2].split())[-1]
fmin=(flist[3].split())[-1]
fmax=(flist[4].split())[-1]
if '0'==iteration_times:#whether this is the first run 
    if 'pass'==judge_innovus_log('workspace'+'_'+iteration_times+'/Innovus/logs'):
        fmax=str(multi_par*int(f))
        fmin=f
        f=str(int(0.5*(int(fmax)+int(fmin))))
        #print f
    else:
        fmax=f
        fmin='0'
        f=str(int(0.5*(int(fmax)+int(fmin))))
        #print f
else:
    if 'pass'==judge_innovus_log('workspace'+'_'+iteration_times+'/Innovus/logs'):
        fmin=f
        f=str(int(0.5*(int(fmax)+int(fmin))))
        #print f
    else:
        fmax=f
        f=str(int(0.5*(int(fmax)+int(fmin))))
        #print f
print   (int(fmax)-int(f))      

if threshold>=(int(fmax)-int(f)):
    rerun='False'
print rerun

flist[0]='rerun '+rerun+'\n'
flist[1]='iteration_times '+str(int(iteration_times)+1)+'\n'
flist[2]='f '+f+'\n'
flist[3]='fmin '+fmin+'\n'
flist[4]='fmax '+fmax+'\n'

f=open('iteration.txt','w+')
f.writelines(flist)
f.close()


