# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
Fill out the count_tags function. It should return a dictionary with the
tag name as the key and number of times this tag can be encountered in
the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.cElementTree as ET
import pprint

data = 'C:\Users\SHLEE\Downloads\seoul_south-korea.osm'

def count_tags(filename):
    data = {'bounds': 0,
            'member': 0,
            'nd': 0,
            'node': 0,
            'osm': 0,
            'relation': 0,
            'tag': 0,
            'way': 0
            }
    database = ET.iterparse(filename)
    database = iter(database)
    for event, elem in database:
        data[elem.tag] += 1
    return data


print count_tags(data)
