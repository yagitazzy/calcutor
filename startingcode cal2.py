

#### TASK 1 - ENTER YOUR TEAM NAME AND NUMBER
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
def sub(num1, num2):
  print("The square root of " + str(number1) + " is " + str(num**0.5))
  return num1 - num2

def sqrt(num):
  print("The square root of " + str(number1) + " is " + str(num**0.5))
  return num**.5

def div(num1, num2):
  print("we are  dividing"+ str(num1) + " and " + str(num2) )
  return num1 / num2
  
def mult(num1, num2):
  print("we are  multiplying" + str(number1) + " and " + str(number2) )
  return num1 * num2
