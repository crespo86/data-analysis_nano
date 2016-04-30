# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""
data = 'C:\Users\SHLEE\Downloads\seoul_south-korea.osm'

def get_user(element):
    for elem in element.attrib:
        if elem == 'uid':
            return element.attrib['uid']

def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if get_user(element) != None:
            users.add(get_user(element))
    return users

print len(process_map(data))
