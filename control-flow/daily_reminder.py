task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
Reminder = ""

match priority:
  case "high" :
    if time_bound == "yes":
       Reminder += f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
  case "low":
    Reminder += f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
  case _:
   Reminder += "Invalid priority level."
print(Reminder) 