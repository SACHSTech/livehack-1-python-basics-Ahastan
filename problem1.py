'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:  The purpose of this program is to make a conversion between the temperature in Fahrenheit to the temperature in Celsius, for my cousin visiting from the U.S

Author:	Surees.A

Created:	07/12/2020
------------------------------------------------------------------------------
'''

# introduce the program to the user 
print ("Welcome to the Fahrenheit to Celsius converter!")

print("")

# ask the user to input the temperature in celsius
celsius_temperature = int(input("What is the temperature in Celsius? "))

# use the proper formula to convert the temperature in celsius to fahrenheit
fahrenheit_temperature = (9/5*celsius_temperature)+ 32

print("")

# Output the proper conversion onto the screen
print ("The temperature you inputted, " + str(celsius_temperature) + "° Celsius is equal to " + str(fahrenheit_temperature) + "° Fahrenheit")