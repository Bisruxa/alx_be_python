Task = input("Enter your task: ")
Priority= input("Pririty (high/medium/low): ")
Time_Bound = input("Is it time-bound? (yes/no): ").lower()

match Time_Bound:
  case Time_Bound if Time_Bound == "yes":
    print(f"Reminder: '{Task}' is a {Priority} priority task that requires immediate attention today! ")
  case Time_Bound if Time_Bound == "no":
    print(f"Note: '{Task}' is a {Priority} priority task. Consider completing it when you have free time. ")
     