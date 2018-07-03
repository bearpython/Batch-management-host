#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import os,sys
import time
import paramiko
import threading
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

HOST_DB = "%s\conf\hostname.json" %BASE_DIR
with open(HOST_DB,"r") as f:
    host_dic = json.load(f)
