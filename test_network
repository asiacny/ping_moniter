#-*- encoding:utf-8 -*-
__author__ = 'Administrator'
import os,time
#This scrpts is written by rffanlab which is only used under linux
from method import *
from build_html import *
from config import *

now = time.strftime("%Y_%m_%d %H:%M:%S", time.localtime())

def main():
    package_sent=""
    package_recived=""
    package_loss=""
    min_time=""
    avg_time=""
    max_time=""
    ips = read_config()
    if len(ips) == 0:
        exit("请在配置文件中至少写入一个测试IP，每行一个IP")
    print ips
    for x in ips:
        if not x.startswith("#"):
            service_provider = x.split(":")[0]
            ip_to_ping = x.split(":")[1].replace("\n","").replace("\r","")
            print "服务商:"+service_provider
            print "IP:"+ip_to_ping
            cmd = "ping "+ip_to_ping+" -c 10"
            print cmd
            ping_result = os.popen(cmd)
            for y in ping_result:
                print y
                if "packets transmitted" in y :
                    package_sent = y.split(",")[0].split(" ")[0]
                    print package_sent
                    package_recived = y.split(",")[1].split(" ")[1]
                    print package_recived
                    package_loss = y.split(",")[2].split(" ")[1]
                    print package_loss
                if y.startswith("rtt"):
                    y_splited = y.split("=")[1].split("/")
                    min_time = y_splited[0].replace(" ","")
                    avg_time = y_splited[1]
                    max_time = y_splited[2]
                    print min_time
                    print avg_time
                    print max_time
            data = "<tr>\n<td>"+package_sent+"</td>\n<td>"+package_recived+"</td>\n<td>"+package_loss+"</td>\n<td>"+min_time+"</td>\n<td>"+avg_time+"</td>\n<td>"+max_time+"</td>\n<td>"+now+"</td>\n</tr>\n</tbody>\n"
            print data
            data_to_change = "</tbody>;</tbody>;"+data
            if os.path.isfile(html_file_path+service_provider+".html"):
                file_opreater(data_to_change,'edit',html_file_path+service_provider+".html")
            else:
                build_html(html_file_path,service_provider,ip_to_ping)
                file_opreater(data_to_change,'edit',html_file_path+service_provider+".html")

if __name__ == '__main__':
    main()


