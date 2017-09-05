# BMEn 5411
# Fall 2017
# Python Tutorial

#This is a comment!

"""
This is also a comment
that allows you to write
on multiple lines.

"""
print("")
print("This is a print statement")
print("")
print("Use these often to debug your code")
print("")
print("________________________________________________")

# if statements

scienceIsFun = True

print("Is science fun?")
print("")

if(scienceIsFun):
    print("Obviously")
    print("")

# while loops

daysLeftOfClass = 25
while (daysLeftOfClass > 0):
   print ('You have this many classes left:', daysLeftOfClass)
   daysLeftOfClass = daysLeftOfClass - 1

grades = ['A','B','C','D','F','FF']

print("________________________________________")
print("")
print("Note the difference between indexing with Matlab vs Python")
print("")
print('Your grade on this assignment is an:',grades[0])
print('Your grade on this assignment is an:',grades[1])
print('Your grade on this assignment is an:',grades[5],".","Don't cheat")

print("________________________________________")
print("")

student_grades = {
        'CC': 100+100,'TN': 100+100,'NA': 0,'WA': 0,'SVSA': 0,'BB': 0,'JB': 0,'TD': 0,'CD': 0,'CD': 0,
        'EG': 0,'PG': 0,'CG': 0,'MG': 0,'AH': 0,'CK': 0,'SK': 0,'ZK': 0,
        'AK': 0,'JL': 0,'LM': 0,'KMai': 0,'KMan': 0,'LM': 0,'DM': 0,'BSRM': 0,
        'ANai': 0,'ANaw': 0,'ATN': 0,'CO': 0,'KP': 0,'JP': 0,'MS': 0,'ES': 0,
        'AS': 0,'SSo': 0,'SSp': 0,'DT': 0,'CZ': 0,'ZZ': 0        
        }

print (student_grades['CC'])

# For loop
for k, v in student_grades.items():
    print(k,v)
    
for i in range(0,10):
    print(i)
    

# Plotting 
import matplotlib.pyplot as plt
    
plt.plot(range(1,10), range(11,20),color='blue',lw=1,label='z(t)')
