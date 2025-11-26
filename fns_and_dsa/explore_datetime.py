from datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("current date and time:", formatted_datetime)
def calculate_future_date():
    try:
         number_of_days = int(input("Enter the number of days to add to the current date: "))
         future_date = datetime.now() + timedelta(days=number_of_days)
         formatted_future_date = future_date.strftime("%Y-%m-%d")
         print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()



