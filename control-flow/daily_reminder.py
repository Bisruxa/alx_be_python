task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match time_bound:
  case time_bound if time_bound == "yes":
    if priority == "high":
     print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today! ")
  case time_bound if time_bound == "no":
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time. ")
     