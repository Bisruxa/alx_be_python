def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  except ValueError:
    print("Error: Please enter numeric values only.")
  else:
    print("The result of the division is", result)
float(numerator) = input("Enter the numerator: ")
float(denominator) = input("Enter the denominator: ")

try:
  type(numerator)!= int or type(denominator) != int
except ValueError:
  print("Error: Please enter numeric values only.")
