# -*- coding: utf-8 -*-
"""Task1_1_217072092.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JSHQsSVWbLX_Zgd6mhH3ZOLqOTvWi47w
"""

#creating a list of weekdays & printing on a new line

weekdaysList = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#collection type
print("weekdaysList:",type(weekdaysList))

#printing the days in weekdaysList on separate lines using for loop
for x in range(len(weekdaysList)):
    print (weekdaysList[x])

#printing a gap to separate sections
print("\t")

#creating a tuple of weekdays & printing
weekdaysTuple = ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#printing days from tuple
print("weekdaysTuple:",type(weekdaysTuple))
for x in range(len(weekdaysTuple)):
    print (weekdaysTuple[x])
#had difficulties in trying to format the print to remove brackets & commas


#printing a gap to separate sections
print("\t")

#creating a tuple of weekdays & printing
weekdaysTuple = ("Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#collection type
print("weekdaysTuple:",type(weekdaysTuple), "experimenting")

#using(len) to count the number of days in the tuple
print('there are ', len(weekdaysTuple), 'days in the week')

#stating what the first day in the tuple is
if "Monday" in weekdaysTuple:
    print("Monday is the first day of the week")

#printing the rest of the days in the tuple
print("the days following it are")
print(weekdaysTuple[1])
print(weekdaysTuple[2])
print(weekdaysTuple[3])
print(weekdaysTuple[4])
print(weekdaysTuple[5])
print(weekdaysTuple[6])
#had difficulties in trying use for loop to print it without brackets/parenthesis

#printing a gap to separate sections
print("\t")

#creating a set of weekdays
weekdaysSet = {"Monday","Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}

#collection type
print("weekdaysSet:",type(weekdaysSet),)
print("These are the days of the week in no particular order")

for x in weekdaysSet:
    print(x)

#printing a gap to separate sections
print("\t")

#creating a dictionary with the days of the week
weekdaysDict = {
    "1":"Monday",
    "2":"Tuesday",
    "3":"Wednesday",
    "4":"Thursday",
    "5":"Friday",
    "6":"Saturday",
    "7":"Sunday"
}
#stating collection type
print("weekdaysDict:",type(weekdaysDict))

#printing Dict items
for keys,values in weekdaysDict.items():
    print(keys,values)

