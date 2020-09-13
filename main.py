# This is a sample Python script Based on CH.3 material
# ASCII text generated with http://www.network-science.de/ascii/
# Donte Jones
# IT Academy @ Emerald Campus
#
#Notes PYCHARM users: Use CTRL+/ to uncomment or comment any selected lines of code




import random

""" 
 _____                 _                 
|  __ \               | |                
| |__) |__ _ _ __   __| | ___  _ __ ___  
|  _  // _` | '_ \ / _` |/ _ \| '_ ` _ \ 
| | \ \ (_| | | | | (_| | (_) | | | | | |
|_|  \_\__,_|_| |_|\__,_|\___/|_| |_| |_|
                                         


Random Int 
Return a number between 0 and 10 (Inclusive, both are included):
"""
#print(random.randint(0, 10))


"""
Random Range 
Returns an integer form a group of numbers starting at 0 up to but not including the number passed
by adding 1 to the output of the function we can change the output
"""
#Example 1
#print(random.randrange(6)) #Produces a number from 0-5 will never produce the number 6 (Exclusive)

#Example 2
#print(random.randrange(6) + 1) #Produces a number from 1 to 6


"""
 ____                       _     _             
|  _ \                     | |   (_)            
| |_) |_ __ __ _ _ __   ___| |__  _ _ __   __ _ 
|  _ <| '__/ _` | '_ \ / __| '_ \| | '_ \ / _` |
| |_) | | | (_| | | | | (__| | | | | | | | (_| |
|____/|_|  \__,_|_| |_|\___|_| |_|_|_| |_|\__, |
                                           __/ |
                                          |___/ 

Branching 
The if statement
Branching gives us the opportunity to execute or skip code based on a condition

for example:
if condition == "true"
    do this
    
Comparison Operators
== Equal to 
!= Not Equal to 
> Greater than
< Less Than 
>= Greater Than or Equal to 
<= Less than or Equal To 

"""
#Example 1 (shorthand notation)
#Change the values of rain and sun to see different results

# rain = True
# sunny = False
# haveUmbrella = False
#
# if rain:
#     print("It is raining...", "\nGetting your umbrella ready.")
#     haveUmbrella = True
#     if haveUmbrella:
#         print("You have your umbrella handy!")
#         print("The value of haveUmbrella is: ", haveUmbrella)
#
# elif sunny:
#     print("Grab your sunglasses")
#     haveUmbrella = False
#     print("The value of haveUmbrella is: ", haveUmbrella)
#
# else:
#     print("It must be cloudy because the value of rain is {}".format(rain),
#           "and the value of sunny is {}".format(sunny))
#
#
# #Example 2 (formatted using longhand)
# money = True
#
# if (money != True):
#     print("i am broke!".title()) #Remember .title() is a string helper method
#
# elif (money == True):
#     print("i am rich!".upper()) #Remember .upper() is a builtin string helper method

"""
__          ___     _ _          _                       
\ \        / / |   (_) |        | |                      
 \ \  /\  / /| |__  _| | ___    | |     ___   ___  _ __  
  \ \/  \/ / | '_ \| | |/ _ \   | |    / _ \ / _ \| '_ \ 
   \  /\  /  | | | | | |  __/   | |___| (_) | (_) | |_) |
    \/  \/   |_| |_|_|_|\___|   |______\___/ \___/| .__/ 
                                                | |    
                                                |_|  


While loops allow the execution of a block of code continuously while the condition remains true 
A Sentinel value is to control when looping should start/stop

Loop structure
Priming Input: initializes just before reaching the loop structure
Check: check the logic that updates the sentinel value
Update: be sure sentinel value will change at some point to prevent an 'Infinite' loop

Infinite Loop:
A loop that can never terminates

Values can be conditions in Python, what does this mean?
If a value exists and does not contain a NULL, EMPTY, or 0 value it can be evaluated as true
Also See Example 1 in the 'Branching' section above

"""
# Example 1 Values as Conditions
# money = float(input("Any value that is not 0 will evaluate as 'True'\nEnter a numeric value to test..."))
#
# if money:
#     print("Money has evaluated to True")
# else:
#     print("Money has evaluated to False")


# Example 2 While loop
#Here is our Prming input
# money = float(input("Any value that is not 0, NONE, NULL, EMPTY will evaluate as 'True'\nEnter a numeric value to test...\n"))
#
# while money: #money is both a 'Condition' and a 'Sentinel' value
#         print("Money has evaluated to True, since you entered {}. You are inside the loop body.".format(money))
#
#         #money gets the opertunity to be upadted so the loop can be terminated at some point
#         money = float(input("Any value that is not 0 will evaluate as 'True'.\nEnter a numeric value to test...\n"))
#
# print("Money has evaluated to False and you have exited the loop body")