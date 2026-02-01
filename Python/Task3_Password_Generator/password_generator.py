import random
import string

print("--- Password Generator ---")

length = int(input("Enter password length: "))

print("Include:")
print("1. Letters")
print("2. Numbers")
print("3. Symbols")

use_letters = input("Letters (y/n): ").lower()
use_numbers = input("Numbers (y/n): ").lower()
use_symbols = input("Symbols (y/n): ").lower()

characters = ""

if use_letters == "y":
    characters += string.ascii_letters
if use_numbers == "y":
    characters += string.digits
if use_symbols == "y":
    characters += string.punctuation

if characters == "":
    print("No character type selected!")
else:
    password = "".join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
