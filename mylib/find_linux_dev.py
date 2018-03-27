#!/usr/bin/env python
#coding: utf-8
import os

# 源目录
deviceFilePath = '/sys/class/input/'

def showDevice():
    os.chdir(deviceFilePath)
    for i in os.listdir(os.getcwd()):
        namePath = deviceFilePath + i + '/device/name'
        if os.path.isfile(namePath):
            print ("Name: %s Device: %s" % (i, file(namePath).read()))
showDevice()