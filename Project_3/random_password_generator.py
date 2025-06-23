import random
import string

# This function displays the main menu to the user
def start_screen():
    print("----------Random Password Generator----------")
    print("1. Alphabetic Password")
    print("2. Numeric Password")
    print("3. Alpha-Numeric Password")

# Generates a password using only letters (both uppercase and lowercase)
def generate_alphabetic_password(length):
    password = ''.join(random.choices(string.ascii_letters, k=length))
    print("Your Alphabetic Password Is:", password)

# Generates a password using only numbers
def generate_numeric_password(length):
    password = ''.join(random.choices(string.digits, k=length))
    print("Your Numeric Password Is:", password)

# Generates a password with both letters and exactly 4 numbers
def generate_alpha_numeric_password(length):
    if length < 4:
        # Make sure the password is long enough to include 4 digits
        print("Password length must be at least 4 to include 4 numbers.")
        return
    alpha_part_length = length - 4  # Calculate how many letters to use
    alpha_part = random.choices(string.ascii_letters, k=alpha_part_length)
    num_part = random.choices(string.digits, k=4)
    password_list = alpha_part + num_part  # Combine letters and numbers
    random.shuffle(password_list)  # Shuffle to mix letters and numbers
    password = ''.join(password_list)
    print("Your Alpha-Numeric Password Is:", password)

# This is the main function that runs the program
def main():
    start_screen()
    try:
        user_input = int(input("Enter your choice (1/2/3): "))
    except ValueError:
        # Handles the case where the user doesn't enter a valid number
        print("Invalid input. Please enter a number (1, 2, or 3).")
        return

    if user_input == 1:
        length = int(input("Enter the length of your password: "))
        generate_alphabetic_password(length)
    elif user_input == 2:
        length = int(input("Enter the length of your password: "))
        generate_numeric_password(length)
    elif user_input == 3:
        length = int(input("Enter the length of your password (recommended > 6): "))
        generate_alpha_numeric_password(length)
    else:
        # Handles any choice that isn't 1, 2, or 3
        print("Invalid choice.")

# This ensures the main function runs only if this file is executed directly
if __name__ == "__main__":
    main()