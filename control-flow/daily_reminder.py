# daily_reminder.py

while True:
    # Prompt for a single task
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    reminder = ""

    # Process the task based on priority and time sensitivity
    match priority:
        case "high":
            if time_bound == "yes":
                reminder += f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                reminder += f"Reminder: '{task}' is a high priority task. Please address it as soon as possible."
        case "medium":
            reminder += f"Reminder: '{task}' is a medium priority task. Plan to complete it soon."
        case "low":
            reminder += f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            reminder += "Invalid priority level. Please enter 'high', 'medium', or 'low'."
            print(reminder)
            continue  # Restart loop if priority is invalid

    # Print the customized reminder
    print(reminder)
    
    # Option to exit or continue
    another = input("Would you like to enter another task? (yes/no): ").lower()
    if another != "yes":
        break
