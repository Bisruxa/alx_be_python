user_prompt = float(input("Enter the temprature to convert: "))
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 


temprature = input("Is this temperature in Celsius or Fahrenheit?(C/F): ").upper()
def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  print(f"{fahrenheit}°F is {celsius:.2f}°C")
  return celsius
def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = 32 + (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) 
  print(f"{celsius}°C is {fahrenheit:.2f}°F")
  return fahrenheit

if temprature == "C":
   convert_to_fahrenheit(user_prompt)
elif temprature == "F":
  convert_to_celsius(user_prompt)
else:
  print("Invalid choice. Please try again.")
   

