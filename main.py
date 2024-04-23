import os  # Importing the 'os' module which provides a way of using operating system dependent functionality.

path = os.path.join(os.path.expanduser("~"), "Documents", "PasswordSaver", "passwords.txt")


def createFolder():
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)


def write_passwords(path):  # Defining a function named write_passwords.
    createFolder()
    while True:
        program_name = input("Enter name of account: ")
        username = input("Enter username or email: ")
        password = input("Enter password: ")
        score = 0
        if program_name != "":
            score += 1
        else:
            print("Error: Account name is empty. You need to write something")
        if username != "":
            score += 1
        else:
            print("Error: Username is empty. You need to write something")
        if password != "":
            score += 1
        else:
            print("Error: Password is empty. You need to write something")
        if score == 3:
            break
    with open(path, "a") as file:
        # Opening a file named "passwords.txt" in append mode, if it doesn't exist, it will be created.
        file.write(f"{program_name}: {username}, {password}\n")
        # Writing the entered username, password, and program name to the file, separated by commas.
    print("Password saved successfully!")  # Printing a success message.


def read_passwords(path):  # Defining a function named read_passwords.
    createFolder()
    if not os.path.exists(path):  # Checking if the file "passwords.txt" does not exist.
        print("No passwords saved yet.")  # Printing a message indicating that no passwords are saved.
        return  # Exiting the function.
    with open(path, "r") as file:  # Opening the file "passwords.txt" in read mode.
        passwords = file.readlines()  # Reading all lines from the file and storing them in the 'passwords' list.
        if not passwords:  # Checking if the 'passwords' list is empty.
            print("No passwords saved yet.")  # Printing a message indicating that no passwords are saved.
            return  # Exiting the function.
        print("Saved passwords:")  # Printing a header for the list of saved passwords.
        for password in passwords:  # Iterating through each line in the 'passwords' list.
            program_name, rest = password.strip().split(': ')
            # Splitting each line by commas and unpacking the values into variables.
            username, password = rest.split(', ')
            print(f"{program_name}: User: {username}, Pass: {password}")
            # Printing the program/website name, username/email, and password.


def delete_passwords(path):
    createFolder()
    if os.path.exists(path):
        print("This will delete all saved passwords!!!")
        while True:
            ask_again = input(f'please write "DeleteAllPasswords" to continue or "cancel" to cancel\n')
            if ask_again == "0":
                continue
            elif ask_again == "DeleteAllPasswords":
                os.remove(path)
                print("All saved passwords deleted successfully!")
                break
            elif ask_again.lower() == "cancel":
                print("canceled")
                main()
                break
            else:
                continue
    else:
        print("No passwords saved yet.")


def main():  # Defining the main function.
    createFolder()
    while True:  # Starting an infinite loop.
        print("\nOptions:")  # Printing options for the user.
        print("1. Write new passwords")
        print("2. See all saved passwords")
        print("998. Delete all saved passwords")
        print("0. Exit")
        choice = input("Enter your choice: ")  # Asking the user to enter their choice.

        if choice == "1":  # Checking if the user chose option 1.
            write_passwords(path)  # Calling the write_passwords function.
        elif choice == "2":  # Checking if the user chose option 2.
            read_passwords(path)  # Calling the read_passwords function.
        elif choice == "998":
            delete_passwords(path)
        elif choice == "0":  # Checking if the user chose option 3.
            print("Exiting...")  # Printing a message indicating that the program is exiting.
            break  # Exiting the loop and ending the program.
        else:  # Handling invalid choices.
            print("Invalid choice. Please enter a valid option.")  # Printing a message indicating an invalid choice.


if __name__ == "__main__":  # Checking if the script is being run directly.
    main()  # Calling the main function.
