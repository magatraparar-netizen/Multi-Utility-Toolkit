import datetime_utils
import math_utils
import random_utils
import uuid_utils
from custom_modules import file_utils, math_tools


def main():
    while True:
        print("\n===================================")
        print(" Welcome to Multi-Utility Toolkit")
        print("===================================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_utils.datetime_menu()

        elif choice == "2":
            math_utils.math_menu()

        elif choice == "3":
            random_utils.random_menu()

        elif choice == "4":
            uuid_utils.generate_uuid()

        elif choice == "5":
            file_utils.file_menu()

        elif choice == "6":
            print("\nDatetime Module:")
            print(dir(datetime_utils))
            print("\nMath Tools Module:")
            print(dir(math_tools))

        elif choice == "7":
            print("Thank you for using Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
