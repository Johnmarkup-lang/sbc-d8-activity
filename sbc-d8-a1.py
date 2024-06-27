from getpass import getpass

def register():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    with open('data-storage.txt', 'r') as file:
        for line in file:
            account, _ = line.strip().split(',')
            if username == account:
                print("Username already exists. Please try again.")
                return

    with open('data-storage.txt', 'a') as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!")
    file.close()

def login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    with open('data-storage.txt', 'r') as file:
        for line in file:
            account, passw = line.strip().split(',')
            if username == account and password == passw:
                print("Login successful!")
                return
        print("Invalid username or password. Please try again.")
        file.close()

def changepass():
    username = input("Enter your username: ")
    old_password = input("Enter your current password: ")
    new_password = input("Enter your new password: ")

    with open('data-storage.txt', 'r') as file:
        lines = file.readlines()

    with open('data-storage.txt', 'w') as file:
        for line in lines:
            account, passw = line.strip().split(',')
            if username == account and old_password == passw:
                file.write(f"{username},{new_password}\n")
                print("Password changed successfully!")
            else:
                ...

def main():
    while True:
        choice = input("Enter '1' to register, '2' to login, '3' to change password: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            changepass()
        else:
            print("Invalid choice. Please try again.")

main()