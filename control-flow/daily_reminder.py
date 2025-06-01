# daily_reminder.py

print("Welcome to your Daily Task Reminder!\n")

# Get task input
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task description cannot be empty. Please try again.")

# Get priority input
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

# Get time sensitivity input
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid input. Please enter 'yes' or 'no'.")

# Match-case block
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is a high priority task. Try to handle it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that still requires attention today!")
        else:
            print(f"\nReminder: '{task}' is a medium priority task. Plan to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task but time-sensitive. Try to fit it in today.")
        else:
            print(f"\nReminder: '{task}' is a low priority task. Consider completing it when you have free time.")
