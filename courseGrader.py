# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import sys

with open('courseGrader.csv', 'a', newline='') as csvfile:
    fieldnames = ['Initials', 'HW1', 'HW2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'Initials': sys.argv[1], 'HW1': sys.argv[2], 'HW2': sys.argv[3]})




