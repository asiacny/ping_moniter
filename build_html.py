#-*- encoding:utf-8 -*-
__author__ = 'Administrator'
import os
from method import *

real_scripts_path = os.path.split(os.path.realpath(__file__))[0]

print real_scripts_path

def build_html(path,service_provider,ip):

    lines = file_opreater('read','read',os.path.join(real_scripts_path,'sample.html'))

    write_file = file_opreater(lines,'write',os.path.join(path,service_provider+".html"))

    data = "<h3>Multiple Headers Sorter</h3>;<h3>Multiple Headers Sorter</h3>;<h3>"+service_provider+"</h3>\n监控IP："+ip
    file_opreater(data,'edit',path+"/"+service_provider+".html")



