import datetime
import time


def current_datetime():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))


def date_difference():
    try:
        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")

        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

        print("Difference:", abs((d2 - d1).days), "days")
    except ValueError:
        print("Invalid date format!")


def format_date():
    now = datetime.datetime.now()
    print("Formatted Date:", now.strftime("%d-%m-%Y"))


def stopwatch():
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    print("Elapsed Time:", round(time.time() - start, 2), "seconds")


def countdown():
    try:
        seconds = int(input("Enter countdown seconds: "))

        if seconds < 0:
            print("Enter a positive number!")
            return

        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1

        print("Time's up!")
    except ValueError:
        print("Please enter a valid number!")


def datetime_menu():
    while True:
        print("\n--- Datetime and Time Operations ---")
        print("1. Display Current Date and Time")
        print("2. Difference Between Two Dates")
        print("3. Format Date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            current_datetime()
        elif choice == "2":
            date_difference()
        elif choice == "3":
            format_date()
        elif choice == "4":
            stopwatch()
        elif choice == "5":
            countdown()
        elif choice == "6":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    datetime_menu()
