import sys
import os
import string
import math
import shutil
import os.path

os.system("sh delete_intermediate_files.sh")


# #read tech_parameters.txt to get golabal parameters
# f=open('tech_parameters.txt','r+')
# flist=f.readlines()

# VDD=flist[0].split()
# VDD=VDD[-1]

# VBIAS=flist[1].split()
# VBIAS=VBIAS[-1]

# BasicDev=flist[2].split()
# BasicDev=BasicDev[-1]

# Liberate_path=flist[3].split()
# Liberate_path=Liberate_path[-1]

# Abstract_path=flist[4].split()
# Abstract_path=Abstract_path[-1]

# PDK_Library=flist[5].split()
# PDK_Library=PDK_Library[-1]

# f.close()


# #running Liberate to get .lib file 
# os.chdir(Liberate_path)
# cmd="sh liberate_run.sh"+' '+VDD+' '+VBIAS+' '+BasicDev
# os.system(cmd)
# os.chdir("../")

#getting fullnames of specified type of files under the specified folder
def get_file_list(folder):
    filelist = []  
    for dirpath,dirnames,filenames in os.walk(folder):
        for file in filenames:
            file_type = file.split('.')[-1]
            if(file_type in file_type_list):
                file_fullname = os.path.join(dirpath, file) #full name of files
                filelist.append(file_fullname)
    return filelist

#copy the files into specified path
def copy_file(src_file_list, dst_folder):
    print('===========copy start===========')
    for file in src_file_list:
        shutil.copy(file, dst_folder)
    print('===========copy end!===========')


#finding all the subfolders in a folder
def finding_subfolder(path):
    list=[]
    #make sure the path exists
    if (os.path.exists(path)):
    #get all the files and sunfolders
        files=os.listdir(path)
        for file in files:
        # get the path of all the paths of dir
            m=os.path.join(path,file)
            #make sure it is a dir
            if(os.path.isdir(m)):
                h=os.path.split(m)
                list.append(h[1])
        print (list)
        return list

 

# #copy .lib file from Libertae to Abstract
# file_type_list = ['lib'] 
# src_folder=Liberate_path+'/lib'
# dst_folder=Abstract_path
# filelist=get_file_list(src_folder)
# copy_file(filelist,dst_folder)


# #copy .lib file into LIB(Genus) and LIBS(Innovus)
# file_type_list = ['lib'] 
# src_folder=Liberate_path+'/lib'
# dst_folder1='LIB'
# dst_folder2='LIBS/lib/max'
# dst_folder3='LIBS/lib/min'
# filelist=get_file_list(src_folder)
# copy_file(filelist,dst_folder1)
# copy_file(filelist,dst_folder2)
# copy_file(filelist,dst_folder3)


#copy LIB LIBS into Genus and Innovus
os.system("cp -r LIB Genus/LIB")
os.system("cp -r LIBS Innovus/LIBS")



# #modify Abstract generator action file "example.record"
# os.chdir(Abstract_path)
# f=open('example.record','r+')
# flist=f.readlines()
# flist[1]='absSetLibrary("'+PDK_Library+'")'+'\n'
# flist[2]='absSetOption("ImportLogicalFiles" '+'"'+BasicDev+'_'+VDD+'_'+'nldm.lib")'+'\n'
# f=open('example.record','w+')
# f.writelines(flist)
# f.close()

# #run Abstract Generator
# AG_cmd="abstract -replay example.record"
# os.system(AG_cmd)
# os.chdir("../")


# #copy .lef file into LEF folder
# file_type_list = ['lef']
# src_folder=Abstract_path
# dst_folder='LEF'
# filelist=get_file_list(src_folder)
# copy_file(filelist,dst_folder)


#copy LEF BasicLEF into Genus and Innovus
os.system("cp -r LEF Genus/LEF")
os.system("cp -r BasicLEF Genus/BasicLEF")

os.system("cp -r LEF Innovus/LEF")
os.system("cp -r BasicLEF Innovus/BasicLEF")


#copy Genus Innovus Design_script.py into each design's folders

Designames=finding_subfolder('Design')

for Designname in Designames:
    while True==os.path.exists('./Design/'+Designname+'/workspace'):
        os.system('rm -r ./Design/'+Designname+'/workspace')
    os.system('mkdir ./Design/'+Designname+'/workspace')
    os.system('cp -r Genus ./Design/'+Designname+'/workspace/Genus')
    os.system('cp -r ./Design/'+Designname+'/RTL ./Design/'+Designname+'/workspace/Genus/RTL')
    os.system('cp -r ./Design/'+Designname+'/SDC ./Design/'+Designname+'/workspace/Genus/SDC')
    os.system('cp -r Innovus ./Design/'+Designname+'/workspace/Innovus')
    os.system('cp Design_script.py ./Design/'+Designname+'/workspace')
    #os.system('cp iteration.txt ./Design/'+Designname+'/workspace')
    os.system('cp -r ./Design/'+Designname+'/iteration.txt ./Design/'+Designname+'/workspace')
    os.system('cp modify_iteration.py ./Design/'+Designname+'/workspace')


#create new terminals for each design and run VLSI flow in each terminals
for Designname in Designames:
    os.chdir('Design/'+Designname+'/workspace')
    #cmd0='python Design_script.py '+Designname
    os.system("gnome-terminal -e 'bash -c \"python Design_script.py; exec bash\"'")
    
    # cmd1='gnome-terminal -e '+"'"+cmd0+"'"
    # print cmd1
    # os.system(cmd1)
    os.chdir("../../..")


