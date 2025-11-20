task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time == "yes":
            print(f"Reminder: 'Finish {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: 'Finish {task}' is a high priority task. Please complete it as soon as possible.")
    case "medium":
        if time == "yes":
            print(f"Reminder: 'Finish {task}' is a medium priority task that should be done soon, preferably today.")
        else:
            print(f"Reminder: 'Finish {task}' is a medium priority task. Try to complete it in the near future.")
    case "low":
        if time == "yes":
            print(f"Reminder: 'Finish {task}' is a low priority task that can be done later today.")
        else:
            print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")


