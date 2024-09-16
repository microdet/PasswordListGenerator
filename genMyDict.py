import itertools
import createDateCodes
import useWordlist


def generate_my_dynamic_list(my_type):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'  # L
    uppercase_letters = lowercase_letters.upper()  # U
    digits = '0123456789'  # D
    spec = ',.#_ !'  # S
    my_characters = ""  # my own character set
    own_chars = "_"  # O

    if 'L' in my_type:
        my_characters = my_characters + lowercase_letters
    if 'U' in my_type:
        my_characters = my_characters + uppercase_letters
    if 'D' in my_type:
        my_characters = my_characters + digits
    if 'S' in my_type:
        my_characters = my_characters + spec
    if 'O' in my_type:
        my_characters = my_characters + own_chars
    if 'A' in my_type:
        my_characters = my_characters + lowercase_letters + uppercase_letters
    if 'X' in my_type:
        my_characters = my_characters + lowercase_letters + uppercase_letters + digits + spec
    # Return the list of characters
    return list(my_characters)


def generate_passwords(my_type, length=1):
    characters = generate_my_dynamic_list(my_type)
    if not characters:
        return []  # No characters available to generate passwords

    # Generate all possible combinations of characters with the given length
    return [''.join(combination) for combination in itertools.product(characters, repeat=length)]


# Define the password pattern
password_parts = [
    ["Andris","Andriska", "Bandi", "Bandika"],                                 # Static string example
    # generate_passwords('L', length=1),          # Dynamic lowcase letter example
    # generate_passwords('S', length=1),          # Dynamic special char example
    # useWordlist.read_and_process_names(r"C:\Users\worka\PycharmProjects\genereatePasswordList\wordlists\nnevek.txt"),
    ["_", ""],
    generate_passwords('D', length=4),          # Dynamic special char example
    #createDateCodes.generate_dates(2, 2000, 1, 1, 2023, 12, 31)
]

# Specify the output file path
output_file = 'An-ka-Ban-ka-4digit.txt'

# Open the file for writing
with open(output_file, 'w', encoding="utf-8") as file:
    # Generate all combinations of parts
    for part in itertools.product(*password_parts):
        my_local_pw = ''.join(part)  # Combine all parts into one password
        file.write(f'{my_local_pw}\n')  # Write password to file, each on a new line

print(f'Passwords have been written to {output_file}')

