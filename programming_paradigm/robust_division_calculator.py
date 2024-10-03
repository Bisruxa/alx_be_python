def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    result = print(f"Error: Cannot divide by zero.")
  return result
float(numerator) = input("Enter the numerator: ")
float(denominator) = input("Enter the denominator: ")
try:
  type(numerator) != int or type(denominator) != int
except ValueError:
  print("Error: Please enter numeric values only.")
