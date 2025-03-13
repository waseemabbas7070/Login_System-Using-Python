# Initialize empty lists to store usernames and passwords
user_names = []
passwords = []

# Get user input for username and password and store them
user_name = input("Enter Your name: ")  # Prompt user for name
password = input("Enter Password: ")   # Prompt user for password

# Append user credentials to the lists
user_names.append(user_name)
passwords.append(password)

# Start an infinite loop for login attempts
while True:
    # Prompt user for login details
    login_name = input("Enter name: ")
    login_password = input("Enter password: ")

    # Check if the entered credentials match stored credentials
    if login_name in user_names and login_password in passwords:
        print("Login Successful!")  # If credentials match, login is successful
        break  # Exit the loop after a successful login
    else:
        print("Sorry, wrong username or password. Try Again!")  # Incorrect credentials message

