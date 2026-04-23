# calcutor: Code that runs user input for the calculator application 
#### TASK 1 - ENTER YOUR TEAM NAME AND NUMBER
import math
team_name = ""

#### TASK 2 - Clone the empty gitHub repo in your local computer (Member #1)

#### TASK 3 - Add this code to your gitHub repo - follow the best practices of add --> commit --> pull --> push

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
      print(f"Sum of your numbers is {addition(num1, num2)}") 
  elif (choice == 2):
      num1 = int(input("what is the first number you want to subtract: "))
      num2 = int(input("what is the second number you want to subtract: "))
      print(f"Difference of your numbers is {sub(num1, num2)}")
  elif (choice == 3):
      num1 = int(input("what is the first number you want to multiply: "))
      num2 = int(input("what is the second number you want to multiply: "))
      print(f"Multiplication of your numbers is {mult(num1, num2)}")
  elif (choice == 4):
      num1 = int(input("what is the first number you want to divide: "))
      num2 = int(input("what is the second number you want to divide: "))
      print(f"Division of your numbers is {div(num1, num2)}")
  elif (choice == 5):
      num1 = int(input("what is the first number you want to integer divide: "))
      num2 = int(input("what is the second number you want to integer divide: "))
      print(f"Integer Division of your numbers is {intdiv(num1, num2)}")
  elif (choice == 6):
      num1 = int(input("what is the number you'd like the square root of: "))
      print(f"Square Root of your number is {sqrt(num1)}")
  elif (choice == 7):
      num1 = int(input("what is the base: "))
      num2 = int(input("What is it to the power of: "))
      print(f"Power of your numbers is {mult(num1, num2)}")
def sub(num1, num2):
  return num1 - num2

def sqrt(num):
  return num**.5

def div(num1, num2):
  return num1 / num2

def intdiv(num1, num2):
    return num1 // num2


def mult(num1, num2):
  return num1 * num2

def exp(num1, num2):
    return math.pow(num1, num2) 
calculator()
