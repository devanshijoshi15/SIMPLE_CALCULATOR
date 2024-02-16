print("TASK 2 - CALCULATOR")
def add(num1, num2):
  """Adds two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers."""
  if num2 == 0:
    return "Error: Cannot divide by zero."
  return num1 / num2

while True:
  # Get user input
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operation = input("Choose an operation (+, -, *, /): ")

  # Perform calculation based on operation choice
  result = None
  if operation == "+":
    result = add(num1, num2)
  elif operation == "-":
    result = subtract(num1, num2)
  elif operation == "*":
    result = multiply(num1, num2)
  elif operation == "/":
    result = divide(num1, num2)
  else:
    result = "Invalid operation."

  # Display the result
  print("Result:", result)

  # Ask if user wants to continue
  choice = input("Do you want to perform another calculation? (y/n): ")
  if choice.lower() != 'y':
    break

print("Calculator closed.")
