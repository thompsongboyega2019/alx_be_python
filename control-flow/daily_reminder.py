task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case ("high"):
        if time_bound == "yes":
             print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to handle it as soon as possible.")
    case ("medium"):
        if time_bound == "yes":
             print(f"Reminder: '{task}' is a medium ih priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to handle it as soon as possible.")
    case ("low"):
        if time_bound == "yes":
             print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Try to handle it as soon as possible.")