
def remove_repeat_chars(string):
    # Initialize an empty list to store the characters of the original string
    char_list = []

    # Iterate over each character in the original string
    for char in string:

        # If the current character is not already in the list of unique characters, append it to the list
        if char not in char_list:
            char_list.append(char)

    # Initialize an empty string to store the altered string
    altered_string = ""

    # Iterate over each character in the original string and append it to the altered string if it is unique
    for char in string:
        if char in char_list:
            altered_string += char

    return altered_string
