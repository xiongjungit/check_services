#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import time
import os
import platform

def getinfo(filename):
    arr = []
    with open(filename,'r') as f:
        for lines in f.readlines():
            lines = lines.replace("\n", "").split(",")
            arr.append(lines[0].split("\t"))
        return arr

def sendemail(msg):
    #smtp服务器信息
    mail_host="mail.cpms.com.cn"
    mail_user="zabbix@cpms.com.cn"
    mail_pass="111111"
    mail_port="25"
    #发件人和收件人
    sender = 'zabbix@cpms.com.cn' #发件人
    receivers = ['xiongjun@cpms.com.cn','liuyanwen@cpms.com.cn',]  #接收人
    #receivers = ['system@cpms.com.cn',]  #接收人
    #创建一个带附件的实例
    message = MIMEMultipart('related')
    message['From'] = Header('zabbix<admin@cpms.com.cn>','utf-8')
    #message['To'] =  Header('熊军<xiongjun@cpms.com.cn>','utf-8')
    message['To'] =  Header('系统组<system@cpms.com.cn>','utf-8')
    subject = '服务状态检测'
    message['Subject'] = Header(subject, 'utf-8')
    #邮件正文内容
    msgAlternative = MIMEMultipart()
    message.attach(msgAlternative)
    mail_msg = msg
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    try:
        #s = smtplib.SMTP_SSL(mail_host,port=mail_port)
        s = smtplib.SMTP(mail_host,port=mail_port)
        s.login(mail_user, mail_pass)
        s.sendmail(sender, receivers, message.as_string())
        s.quit()
        print "邮件发送成功!"
    except smtplib.SMTPException,e:
        print "邮件发送失败,%s" % e
        pass

def tohtml(filename):
    info = getinfo(filename)
    with open('index.html','w+') as f:
        print >> f, "<style>"
        print >> f, "table,table tr th, table tr td { border:1px solid blue; }"
        #print >> f, "table,table tr th, table tr td { border:1px solid red; }"
        print >> f, "table { width: 680px; min-height: 25px; line-height: 25px; text-align: center; border-collapse: collapse; padding:2px;}"
        print >> f, "</style>"
        print >> f, "<table border=\"1\">"
        print >> f, "<tr>"
        print >> f, "<th>序号</th>"
        print >> f, "<th>日期</th>"
        print >> f, "<th>时间</th>"
        print >> f, "<th>服务名</th>"
        print >> f, "<th>服务别名</th>"
        print >> f, "<th>IP</th>"
        print >> f, "<th>端口</th>"
        print >> f, "<th>状态</th>"
        print >> f, "</tr>"
        SN = 0
        for list in info:
            print >> f, "<tr>"
            SN += 1
            Date = list[0].split(" ")[0]
            Time = list[0].split(" ")[1]
            Name = list[0].split(" ")[2]
            Alias = list[0].split(" ")[3]
            IP = list[0].split(" ")[4]
            Port = list[0].split(" ")[5]
            Status = list[0].split(" ")[6]
            print >> f, "<td>%s</td>" %SN
            print >> f, "<td>%s</td>" %Date
            print >> f, "<td>%s</td>" %Time
            print >> f, "<td>%s</td>" %Name
            print >> f, "<td>%s</td>" %Alias
            print >> f, "<td>%s</td>" %IP
            print >> f, "<td>%s</td>" %Port
            print >> f, "<td><font color=red>%s</font></td>" %Status
            print >> f, "</tr>"
        print >> f, "</table>"

def main():
    if platform.system() == "Windows":
        logfile = "logs\\check.log"
    else:
        logfile = "logs/check.log"
    if os.path.exists(logfile):
        filesize = os.path.getsize(logfile)
        if filesize != 0:
            tohtml(logfile)
            with open('index.html','r') as f:
                msg = f.read()
                sendemail(msg)

if __name__ == "__main__":
    main()
