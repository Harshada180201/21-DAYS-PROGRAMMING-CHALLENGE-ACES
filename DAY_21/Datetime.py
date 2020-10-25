
from datetime import *

a = datetime.now()
print(a)   # prints current time 
# ************************************************
a = datetime.now()
print(a.month)
print(a.strftime("%b"))  # formats date objects into readable strings
# *************************************************
x = datetime(2018, 6, 22)  # time is optional
x = datetime(2018, 6, 22 ,22 ,11 ,10) # with time
print(x)
print(x.strftime("%a"))
# ********************************************************
import calendar
cal = calendar.month(2010, 1)
print("Here is the calendar:")
print(cal) 