#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import os,sys
import time
import paramiko
import threading

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting

class Hosts(object):
    """host主机类、组、用户名、密码"""
    def __init__(self,host,port,user,passwd,cmd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.cmd = cmd

    def base(self):
        """类内部首先要执行的方法，来判断一下用户输入进来的命令是什么，然后去执行"""
        cmd_str = self.cmd.split()[0]
        if hasattr(self,cmd_str):  #判断这个类内部是否有用户输入的方法名
            func = getattr(self,cmd_str )
            func()
        else:
            setattr(self,cmd_str,self.command)  #到这里是输入的指令在类内部找不到相同的方法，就给他赋值一个方法名，然后在由getattr调用
            func = getattr(self, cmd_str)
            func(self.cmd)

    def command(self,command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, port=self.port, username=self.user, password=self.passwd)
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode()
        err = stderr.read()
        print( "-------------------HOST:%s-------------------\n" %(self.host) ,result, err)
        ssh.close()

    def put(self):
        """批量分发文件"""
        transport = paramiko.Transport(self.host,self.port)  # ftp
        transport.connect(username=self.user, password=self.passwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put('%s\data\\windows7' %(setting.BASE_DIR), '/tmp/windows7.text')
        # 将remove_path 下载到本地 local_path
        #sftp.get('/tmp/centos6.5.text', '%s\data\\centos6.5.text' %(setting.BASE_DIR))
        transport.close()

def show_host():
    """用户登陆后的首界面，打印主机组列表"""
    # print(setting.host_dic)
    host_group_list = []
    for i in setting.host_dic:  # 字典的循环
        print("主机组名称：%s  主机数量：[%s]" %(i, len(setting.host_dic[i])))
        host_group_list.append(i)
    while True:
        user_chose = input("请输入主机组名称(退出程序请输入B)：").strip()
        if len(user_chose) == 0: continue
        if user_chose == "B":return user_chose
        if user_chose in host_group_list:
            for key in setting.host_dic[user_chose]:
                print("主机名称：%s IP地址：%s" %(key,setting.host_dic[user_chose][key]["ip"]))
            # print(setting.host_dic[user_chose])
            grouping_host_dic = setting.host_dic[user_chose]
            return grouping_host_dic
        else:
            print("您输入的主机组名称错误，请重新输入")

def interactive(grouping_host_dic):
    """具体用户要执行的命令，起多线程去执行，返回结果"""
    while True:
        user_command = input("输入要操作的指令(返回上一级请输入B)：").strip()
        if len(user_command) == 0:continue
        if user_command == "B":
            break
        t_odbjs = []
        for i in grouping_host_dic:
            host,user,passwd = grouping_host_dic[i]["ip"],grouping_host_dic[i]["user"],grouping_host_dic[i]["passwd"]
            func = Hosts(host,22,user,passwd,user_command)
            t = threading.Thread(target=func.base)
            t.start()
            t_odbjs.append(t)
        # for i in t_odbjs:
        #     i.join()
        while threading.active_count() != 1:
             pass

def run():
    """程序逻辑的入口，首先调用打印host列表，得到主机的配置信息"""
    while True:
        choose_hosts = show_host()
        if choose_hosts == "B":
            print("程序安全退出！")
            break
        interactive(choose_hosts)