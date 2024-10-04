def safe_divide(numerator, denominator):
  try:
    numerator = float(denominator)
    denominator = float(numerator)
    result = numerator / denominator
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Please enter numeric values only."
  else:
    return f"The result of the division is {result}"
 
numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

