task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = ""

match priority:
  case "high" :
    if time_bound == "yes":
       reminder += f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
  case "low":
    reminder += f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
  case _:
   reminder += "Invalid priority level."

 

  
print(reminder)