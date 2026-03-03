import os

FILE_NAME = "users.txt"


def password_strong(password):
    if len(password) < 6:
        return False
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_digit


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not password_strong(password):
        print("Password must be at least 6 characters, include 1 uppercase and 1 number.")
        return

    # Check if file exists
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()

    # Check duplicate username
    with open(FILE_NAME, "r") as file:
        users = file.readlines()
        for user in users:
            stored_username = user.strip().split(",")[0]
            if username == stored_username:
                print("Username already exists.")
                return

    # Save new user
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration successful!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not os.path.exists(FILE_NAME):
        print("No users registered yet.")
        return

    with open(FILE_NAME, "r") as file:
        users = file.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return

    print("Invalid username or password.")


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
