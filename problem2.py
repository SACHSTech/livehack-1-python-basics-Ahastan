'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:  The purpose of this program is to find out how many pieces of chicken each student would get, and how many pieces of chicken Mr. Fabroa would get.

Author:	Surees.A

Created:	07/12/2020
------------------------------------------------------------------------------
'''

# welcome the user to the program
print ("Welcome to the Popeyes Chicken distrubutor!")

print ("")

# ask the user to input how many students are in the class
students = int(input("How many students are in the class? "))

print("")

# ask the user how many pices of chicken are being distributed
pieces_of_chicken = int(input("How many pieces of chicken are being given to the students? "))

print("")

# determine how many pieces of chicken each student will get
pieces_per_student = pieces_of_chicken / students

# determine how many pieces of chicken Mr. Fabroa would get
mrFabroa_chicken = pieces_of_chicken % students

# output the number of chicek each would get
print ("The students would get " + str(pieces_per_student) + " pieces of chicken and Mr. Fabroa would get " + str(mrFabroa_chicken) + " pieces of chicken. ")