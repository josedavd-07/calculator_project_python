
"""
#calculator for addition, subtraction, multiplication and division
import colorama
#import colorama
from colorama import Fore, Back, Style
colorama.init()


"""
#Calculator sum
"""
#use the function to sum two numbers
def addition(number1, number2):
    return number1 + number2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

#control input data
if number1 and number2 >= 1:
    print("The sum is: ", addition(number1, number2))
elif number1 and number2 < 1:
    print("The number is less than 1")
else:
    print=("Invalid number")


"""









# Calculator for addition, subtraction, multiplication, and division
import colorama
from colorama import Fore
colorama.init()

"""
Calculator sum
"""
# Use the function to sum two numbers
def addition(number1, number2):
    return number1 + number2

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Control input data
if number1 >= 1 and number2 >= 1:
    print(Fore.GREEN + "The sum is:", addition(number1, number2))
elif number1 < 1 or number2 < 1:
    print(Fore.RED + "The number is less than 1")
else:
    print(Fore.RED + "Invalid number")
