num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = 0
operation = input("Choose the operation (+, -,*, /): ")
match operation:
  case operation if operation == "+":
    result = num1 + num2
    print(f"The result is {result}")
  case operation if operation == "-":
    result = num1 - num2
    print(f"The result is {result}")
  case operation if operation == "*":
   result = num1 * num2
   print(f"The result is {result}")
  case operation  if operation == "/":
    
    if(num2 == 0):
      print("Cannot divide by zero")
    else:
     result = num1 / num2
     print(f"The result is {result}")