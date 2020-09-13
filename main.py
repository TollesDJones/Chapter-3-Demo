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
if condition == "true"
    do this
"""
#Example 1 (shorthand notation)
#Change the values of rain and sun to see different results

rain = False
sunny = False
haveUmbrella = False

if rain:
    print("It is raining...", "\nGetting your umbrella ready.")
    haveUmbrella = True
    if haveUmbrella:
        print("You have your umbrella handy!")
        print("The value of haveUmbrella is: ", haveUmbrella)

elif sunny:
    print("Grab your sunglasses")
    haveUmbrella = False
    print("The value of haveUmbrella is: ", haveUmbrella)

else:
    print("It must be cloudy because the value of rain is {}".format(rain),
          "and the value of sunny is {}".format(sunny))


#Example 2 (formatted using longhand)
money = True
if ( money != True):
    print("i am broke!".title()) #Remember .title() is a string helper method

elif (money == True):
    print("i am rich!".upper()) #Remember .upper() is a builtin string helper method
