
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 


def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}°F is {celsius}°C")
  return celsius
def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR + 32 * celsius 
  print(f"{celsius}°C is {fahrenheit}°F")
  return fahrenheit
user_prompt = float(input("Enter the temperature to convert: "))
temprature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if temprature == "C":
   convert_to_fahrenheit(user_prompt)
elif temprature == "F":
  convert_to_celsius(user_prompt)
else:
  print("Invalid choice. Please try again.")
   

