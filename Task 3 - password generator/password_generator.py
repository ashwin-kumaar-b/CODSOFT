import random
import string

def generate_password(length, complexity):
    if length < 4:
        return "Password length should be at least 4 characters."

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


try:
    length = int(input("Enter the desired password length: "))

    print("\nChoose complexity level:")
    print("1 - Letters only (a-z, A-Z)")
    print("2 - Letters + Numbers (a-z, A-Z, 0-9)")
    print("3 - Letters + Numbers + Symbols (a-z, A-Z, 0-9, !@#$...)")
    complexity = int(input("Your choice (1/2/3): "))

    password = generate_password(length, complexity)
    print(f"\nGenerated Password: {password}")
except ValueError:
    print("❌ Please enter valid numeric input.")
