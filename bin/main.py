#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author:bear

import os,sys,socketserver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import management


if __name__ == "__main__":
    management.run()
