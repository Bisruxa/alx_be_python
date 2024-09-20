task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = ""
prio=""
match priority:
  case "high":
    prio += "high priority task"
  case "low":
    prio += "low priority task."
  case _:
    prio += "Invalid priority level"
if time_bound == "yes":
  reminder += f"Reminder: '{task}' is a " + prio + " that requires immediate attention today!"
else:
  reminder += f"Note: '{task}' is a "+ prio + "Consider completing it when you have free time."
print(f"reminder")