task = input("Enter your task: ")
priority= input("Pririty (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").lower()

match time_bound:
  case time_bound if time_bound == "yes":
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today! ")
  case time_bound if time_bound == "no":
    print(f"Note: 'Read a book' is a low priority task. Consider completing it when you have free time. ")
     