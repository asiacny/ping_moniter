#-*- encoding:utf-8 -*-
__author__ = 'Administrator'
import os
real_scripts_path = os.path.split(os.path.realpath(__file__))[0]

def read_config():
    file = open(real_scripts_path+'/ip.conf',"r")
    lines = file.readlines()
    file.close()
    return lines



def file_opreater(data,action,file_path):
    lines =[]
    if action =='read':
        myfile = open(file_path,'r')
        lines = myfile.readlines()
        myfile.close()
    elif action == 'write':
        myfile = open(file_path,'w')
        myfile.writelines(data)
        myfile.close()
    elif action =='add':
        myfile = open(file_path,'a')
        myfile.writelines(data)
        myfile.close()
    elif action =='edit':
        myfile = open(file_path,'r')
        lines = myfile.readlines()
        myfile.close()
        for num in xrange(len(lines)):
            if data.split(";")[0] in lines[num]:
                lines[num]=lines[num].replace(data.split(";")[1],data.split(";")[2])
        myfile = open(file_path,'w')
        myfile.writelines(lines)
        myfile.close()
    if lines:
        return lines
