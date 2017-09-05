# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
students = {}

with open('Book1.csv') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for row in spamreader:
        students[row["Initials"]] = row["Grade"]

'''
import csv
import sys

with open('courseGrader.csv', 'a', newline='') as csvfile:
    fieldnames = ['Initials', 'HW1', 'HW2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'Initials': sys.argv[1], 'HW1': sys.argv[2], 'HW2': sys.argv[3]})

student_grades = {
        'NA': 0,'WA': 0,'SVSA': 0,'BB': 0,'JB': 0,'TD': 0,'CD': 0,'CD': 0,
        'EG': 0,'PG': 0,'CG': 0,'MG': 0,'AH': 0,'CK': 0,'SK': 0,'ZK': 0,
        'AK': 0,'JL': 0,'LM': 0,'KMai': 0,'KMan': 0,'LM': 0,'DM': 0,'BSRM': 0,
        'ANai': 0,'ANaw': 0,'ATN': 0,'CO': 0,'KP': 0,'JP': 0,'MS': 0,'ES': 0,
        'AS': 0,'SSo': 0,'SSp': 0,'DT': 0,'CZ': 0,'ZZ': 0        
        }

