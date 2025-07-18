task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority
match priority:
    case "high":
        msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        msg = f"Reminder: '{task}' is a medium priority task"
    case "low":
        msg = f"Note: '{task}' is a low priority task"
    case _:
        msg = f"Error: Invalid priority for '{task}'"

# Time-bound check
if time_bound == "yes":
    print(f"{msg} that requires immediate attention today!")
elif time_bound == "no":
    print(f"{msg}. Consider completing it when you have free time.")
else:
    print("Error: Time-bound response must be 'yes' or 'no'.")
