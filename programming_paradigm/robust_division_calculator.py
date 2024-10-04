def safe_divide(numerator, denominator):
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    result = "Error: Cannot divide by zero."
  except ValueError:
    result ="Error: Please enter numeric values only."
  else:
    result = f"The result of the division is {result}"
  return result
numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

float(denominator)
float(numerator)