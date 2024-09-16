#PasswordListGenerator
This code is for study purposes. 
It demonstrates how to create a .txt file containing passwords according to a specified pattern.

#Features
Generate passwords using predefined character sets.
Supports both static strings and dynamically generated sequences.
Create passwords with mixed patterns, such as letters, digits, and custom date formats.
Use wordlists to generate names or other predefined patterns.
Predefined Character Lists.
Merge or split the gernerated file according to the size of need.


The following character lists are used in the pattern generation:
  lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'  # L
  uppercase_letters = lowercase_letters.upper()  # U
  digits = '0123456789'  # D
  spec = ',.#_ !'  # S
These lists are referenced using simple characters (like L for lowercase letters or D for digits) in the pattern.


#Pattern Structure
The pattern can include both static strings and dynamically generated sequences. Here’s an example breakdown:

password_parts = [
    ["Almafa"],  # Static string example
    generate_passwords('L', length=1),  # Dynamic 1 character lowercase letter
    generate_passwords('D', length=2),  # Dynamic 2 character digits
    useWordlist.read_and_process_names(r"C:\Users\worka\PycharmProjects\genereatePasswordList\wordlists\nnevek.txt"),  # Names from a wordlist (Hungarian female names), capitalized
    ["_", ""],  # Optional user-determined character (underscore or empty)
    createDateCodes.generate_dates(4, 2000, 1, 1, 2023, 12, 31)  # Dynamic date generator
]

#Dynamic Examples
  Static String Example: "Almafa"
  A fixed string that will always appear in the password at that specific place.

  Dynamic Lowercase Letter Example: generate_passwords('L', length=1)
  Generates a single lowercase letter based on the L pattern.
  
  Dynamic Digits Example: generate_passwords('D', length=2)
  Generates a sequence of two digits.

  Wordlist Example: useWordlist.read_and_process_names("path/to/names.txt")
  Generates names from a wordlist (e.g., Hungarian female names), with the first letter capitalized and the rest in lowercase.

  Optional Character: ["_", ""]
  A character that is optional, allowing either an underscore _ or nothing.

#Date Example:
  The createDateCodes.generate_dates function generates dates in various formats. You can choose whether the year should be represented with 2 digits or 4 digits.
  
  For example:
  2-digit year: 23 for the year 2023
  4-digit year: 2023
  The function allows flexibility in date formats, depending on your requirements.

#Output Example
  Sample generated passwords might look like:

  Almafaa00_20201001
  ...
  Almafaz9920241231
