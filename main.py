# This is a sample Python script.

import random

""" 
Random Int 
Return a number between 0 and 10 (Inclusive, both are included):
"""
#print(random.randint(0, 10))


"""
Random Range 
Returns an integer form a group of numbers starting at 0 up to the number passed
by adding 1 to the output of the function we can change the output
"""
#Example 1
#print(random.randrange(6)) #Produces a number from 0-5 will never produce the number 6 (Exclusive)

#Example 2
#print(random.randrange(6) + 1) #Produces a number from 1 to 6


"""
Branching 
The if statement
Branching gives us the opportunity to execute or skip code based on a condition

for example:
if raining == "true"
    do some special action
"""


runs = 6
for i in range(runs):
    print(random.randrange(6)+1)

