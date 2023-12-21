
def remove_repeat_chars(s):
    # Initialize an empty list to store the characters of the string
    char_list = []
    # Iterate over each character in the string
    for c in s:
        # If the current character is not already in the list of unique characters
        if c not in char_list:
            # Add the current character to the list of unique characters
            char_list.append(c)
    # Initialize an empty string to store the altered string
    altered_string = ""
    # Iterate over each character in the list of unique characters
    for c in char_list:
        # Add the current character to the altered string
        altered_string += c
    return altered_string
