
import math
team_name = "Ben_Shamia_Ian"



def addition(number1, number2):
  print("We are adding " + str(number1) + " and " + str(number2))
  return number1 + number2


def calculator():
  print("Calculator by team =  " + team_name)
  print("Choose the operation you want to perform: ")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Integer Division")
  print("6. Square Root")
  print("7. Exponent")

 choice = int(input("Enter your choice: "))
if (choice == 1):
  print("what is the first number you want to add?") 
  num1 = int(input("what is the first number you want to add: "))
  num2 = int(input("what is the second number you want to add: "))
  addition(num1, num2) 
elif (choice == 2):
  num1 = int(input("what is the first number you want to subtract: "))
  num2 = int(input("what is the second number you want to subtract: "))
  div(num1, num2)
elif (choice == 3):
  num1 = int(input("what is the first number you want to multiply: "))
  num2 = int(input("what is the second number you want to multiply: "))
  mult(num1, num2)



calculator()


def div(num1, num2):
  return num1 / num2
  

