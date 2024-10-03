def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    result = print(f"Error: Cannot divide by zero.")
  return result
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))
try:
  type(num1) != int or type(num2) != int
except ValueError:
  print("Error: Please enter numeric values only.")
