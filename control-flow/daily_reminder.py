task = input("Enter your task: ")
priority= input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
  case priority if priority == "high"  and time_bound == "yes":
   print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today! ")
  case priority if priority == "low":
    print(f"Note: '{task}' is a {priority} priority task.  Consider completing it when you have free time. ")
     