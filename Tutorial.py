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