task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an invalid priority level"

if time_bound == "yes":
    print(f"Reminder: {reminder} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: {reminder}. Consider completing it when you have free time.")
else:
    print("Error: Time-bound response must be 'yes' or 'no'.")
