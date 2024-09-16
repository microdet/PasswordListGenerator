def read_and_process_names(file_path):
    # Initialize an empty list to store the names
    names_list = []

    # Open the file for reading
    with open(file_path, 'r', encoding='utf-8') as file:
        # Read each line from the file
        for line in file:
            # Strip any leading/trailing whitespace characters
            name = line.strip()
            # Convert the name to title case (only the first letter capitalized)
            title_case_name = name.capitalize()
            # Append the processed name to the list
            names_list.append(title_case_name)

    return names_list


def test_my_wordlist():
    file_path = r"C:\Users\worka\PycharmProjects\genereatePasswordList\wordlists\nnevek.txt"
    processed_names = read_and_process_names(file_path)
    return processed_names


# For test uncomment the next lines.
# my_test_list = test_my_wordlist()
# print(my_test_list)
