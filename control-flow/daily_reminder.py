
task = input("Enter the task description: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

reminder_message = ""


match priority:
    case "high":
        reminder_message = f"CRITICAL REMINDER: You have a High priority task: '{task}'"
    case "medium":
        reminder_message = f"REMINDER: You have a Medium priority task: '{task}'"
    case "low":
        reminder_message = f"NOTE: You have a Low priority task: '{task}'"
    case _:
        reminder_message = f"You have a task with unspecified priority: '{task}'"


if time_bound == "yes":
    
    reminder_message += " that requires immediate attention today!"
else:
    reminder_message += "."


print("-" * 30)
print(reminder_message)
print("-" * 30)