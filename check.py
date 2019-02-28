#!/usr/bin/env python
#coding:utf-8
import requests
import time
import logging
import sys
import os
import conf
import ssh
import sendmail
import platform

def local_time():
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return local_time

def usage():
    filename = sys.argv[0]
    if len(sys.argv) < 2:
        print "Usage: python %s service_name service_url" % filename
        sys.exit(1)

def timmer(func):
    def wrapper(*args,**kwargs):
        print('programe strat running...')
        start = time.time()
        try:
            result = func(*args,**kwargs)
            end = time.time()
            runtime = end - start
            print('running %s s'%runtime)
            return result
        except:logging.error('programe running err!')
        finally: print('programe end running!\n')
    return wrapper

# @timmer
def check_service(service_name,service_url,logfile):
    try:
        req = requests.get(service_url,timeout=3)
        http_status_code = req.status_code
        http_header =  req.headers
        # if "Content-Type" in http_header and http_status_code == 200:
        if "Content-Type" in http_header:
            pass
            # print local_time(),name,ip,port,"up"
        else:
            print local_time(), name, alias, ip, port, "down"
            with open(logfile,'a+') as f:
                print >> f, local_time(), name, alias, ip, port, "down"
            #ssh.run(ip,name)
    except Exception as e:
        print local_time(),name,ip,port,"down"
        with open(logfile,'a+') as f:
            print >> f, local_time(), name, alias, ip, port, "down"
        #ssh.run(ip,name)

if __name__ == "__main__":
    if "Windows" in platform.architecture():
        logfile = "logs\check.log"
    else:
        logfile = "logs/check.log"
    Time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    if os.path.exists(logfile):
        os.rename(logfile,'%s_%s' %(logfile,Time))
    config_file = conf.getConfig("service.ini")
    sections = conf.getSections(config_file)
    # print "日期","时间","服务","主机","端口","状态"
    for service_name in sections:
        items = conf.getItems(config_file,service_name)
        name = items[0][1];alias = items[1][1];protocol = items[2][1];ips = (items[3][1]).split(",");port = items[4][1];index = items[5][1]
        for ip in ips:
            service_url = protocol + "://" + ip + ":" + port + "/" + index
            check_service(service_name,service_url,logfile)
    sendmail.main()







