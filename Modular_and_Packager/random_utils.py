
import random
import string


def random_number():
    try:
        start = int(input("Enter minimum number: "))
        end = int(input("Enter maximum number: "))

        if start > end:
            print("Minimum must not exceed maximum.")
        else:
            print("Random Number:", random.randint(start, end))
    except ValueError:
        print("Please enter valid integers!")


def random_list():
    try:
        count = int(input("How many numbers? "))

        if count <= 0:
            print("Enter a positive count.")
            return

        numbers = [random.randint(1, 100) for _ in range(count)]
        print("Random List:", numbers)
    except ValueError:
        print("Please enter a valid integer!")


def random_password():
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(
            random.SystemRandom().choice(characters)
            for _ in range(length)
        )
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid length!")


def random_otp():
    print("Generated OTP:", random.SystemRandom().randint(100000, 999999))


def random_sampling():
    items = input("Enter items separated by commas: ").split(",")
    items = [item.strip() for item in items if item.strip()]

    if not items:
        print("Please enter some items.")
        return

    try:
        count = int(input("How many items to select? "))

        if count < 1 or count > len(items):
            print("Count must be between 1 and", len(items))
        else:
            print("Random Sample:", random.sample(items, count))
    except ValueError:
        print("Please enter a valid number!")


def random_menu():
    while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            random_number()
        elif choice == "2":
            random_list()
        elif choice == "3":
            random_password()
        elif choice == "4":
            random_otp()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    random_menu()
