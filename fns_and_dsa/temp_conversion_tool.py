FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
user_prompt = float(input("Enter the temprature to convert: "))
temprature = input("Is this temperature in Celsius or Fahrenheit?(C/F): ").upper()
def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  celsius = (FAHRENHEIT_TO_CELSIUS_FACTOR * fahrenheit) + 32
  result= print(f"{user_prompt}degree is {celsius}")
  return result
def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) - 32
  result=print(f"{user_prompt}degree is {fahrenheit}")
  return result

if temprature == "C":
   convert_to_celsius(user_prompt)
elif temprature == "F":
  convert_to_fahrenheit(user_prompt)
 
  
else:
  print("Invalid choice. Please try again.")
   

