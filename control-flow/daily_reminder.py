task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an invalid priority"

if time_bound == "yes":
    print(f"{reminder} that requires immediate attention today!")
elif time_bound == "no":
    print(f"{reminder}. Consider completing it when you have free time.")
else:
    print("Invalid time-bound response. Use 'yes' or 'no'.")
