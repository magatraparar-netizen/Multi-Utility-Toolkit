from pathlib import Path

FILE_NAME = Path(__file__).with_name("toolkit_notes.txt")


def create_file():
    if FILE_NAME.exists():
        print("File already exists!")
    else:
        FILE_NAME.touch()
        print("File created successfully!")


def write_file():
    text = input("Enter text to save: ")

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(text + "\n")

    print("Text saved successfully!")


def read_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()

        if content:
            print("\nFile Content:\n", content)
        else:
            print("File is empty.")

    except FileNotFoundError:
        print("File not found. Please create a file first.")


def update_file():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read()

        if not content:
            print("File is empty. Nothing to update.")
            return

        print("\nCurrent File Content:\n", content)

        old_text = input("Enter text to replace: ")

        if old_text not in content:
            print("Text not found in file.")
            return

        new_text = input("Enter new text: ")
        content = content.replace(old_text, new_text)

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write(content)

        print("File updated successfully!")

    except FileNotFoundError:
        print("File not found. Please create a file first.")


def file_menu():
    while True:
        print("\n===== File Operations =====")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Update a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            update_file()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    file_menu()