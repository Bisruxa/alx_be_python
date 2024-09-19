task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
if time_bound == "yes":
  reminder = f"Reminder: '{task}' is a "
else:
  reminder = f"Note: '{task}' is a "

match priority:
  case "high" :
   reminder += "high priority task "
  case "low":
    reminder += "low priority task. "
  case _:
    reminder += "Invalid priority level."
if time_bound == "yes":
  reminder += f"that requires immediate attention today"
else:
  reminder += f"Consider completing it when you have free time."
print(reminder)