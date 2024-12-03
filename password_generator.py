
import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    # Get user preferences
    length = int(input("Enter the desired password length: "))
    include_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    
    # Define character pools
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Build the character set based on preferences
    char_set = letters
    if include_numbers:
        char_set += numbers
    if include_symbols:
        char_set += symbols
    
    if length < 1 or not char_set:
        print("Invalid input. Please try again.")
        return
    
    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    generate_password()
