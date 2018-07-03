#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear


import json,sys,os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_DIR)
# print(BASE_DIR)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

acc_dic = {
    "group1":{"sit-01":
            {
            "ip":"172.18.1.106",
            "user":"root",
            "passwd": "123456",
            },
        "sit-02":
            {
                "ip": "172.18.1.107",
                "user": "root",
                "passwd": "123456",
            },
    },
    "group2":
        {"sit-03":
            {
            "ip": "172.18.1.108",
            "user": "root",
            "passwd": "123456",
            },
        },
}

# acc_dic2 = {
#     "hostname": "sit-02",
#     "ip":"172.18.1.107",
#     "user":"root",
#     "passwd": "666666",
#     "group": "app",
# }
#
# acc_dic3 = {
#     "hostname": "sit-03",
#     "ip":"172.18.1.108",
#     "user":"root",
#     "passwd": "654321",
#     "group": "phone",
# }

# print(json.dumps(acc_dic))
# username = acc_dic["name"]


with open("%s\conf\hostname.json" %(BASE_DIR),"w") as f:
    f.write(json.dumps(acc_dic))
