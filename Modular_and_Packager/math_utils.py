import math


def factorial():
    number = int(input("Enter a number: "))
    print("Factorial:", math.factorial(number))


def compound_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate: "))
    time = float(input("Enter time in years: "))

    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal

    print("Compound Interest:", round(interest, 2))
    print("Total Amount:", round(amount, 2))


def trigonometry():
    angle = float(input("Enter angle in degrees: "))
    radians = math.radians(angle)

    print("Sin:", round(math.sin(radians), 4))
    print("Cos:", round(math.cos(radians), 4))
    print("Tan:", round(math.tan(radians), 4))


def area_shapes():
    print("\n1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Choose shape: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        print("Circle Area:", round(math.pi * radius ** 2, 2))

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Rectangle Area:", length * width)

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Triangle Area:", 0.5 * base * height)

    else:
        print("Invalid choice!")


def math_menu():
    while True:
        print("\n===== MATH UTILITIES =====")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            factorial()
        elif choice == "2":
            compound_interest()
        elif choice == "3":
            trigonometry()
        elif choice == "4":
            area_shapes()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    math_menu()