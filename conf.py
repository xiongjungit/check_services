#!/usr/bin/env python
# coding:utf-8

import ConfigParser
import sys
import os
import platform

def getConfig(config_name):
    path = os.path.dirname(os.path.abspath(sys.argv[0]))
    if "Windows" in platform.architecture():
        config_file = path + '\%s' %config_name
    else:
        config_file = path + '/%s' %config_name
    return config_file

def getSections(config_file):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    sections = config.sections()
    return sections

def getOptions(config_file,service_name):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    options = config.options(service_name)
    return options

def getItems(config_file,service_name):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    items = config.items(service_name)
    return items

if __name__ == "__main__":
    pass

