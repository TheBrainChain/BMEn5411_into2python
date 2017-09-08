# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:37:08 2017

@author: BME_HeLab
"""
import sys
import csv
import collections

import numpy as np

students = {}

with open('courseGrader.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        students[row["Initials"]] = OrderedDict(int(row["HW1"]),int(row["HW2"]))
      
        
#a = np.ndarray.mean(students['CC'])
print(np.mean(students['XX']))
#print(a)

print(students.keys())