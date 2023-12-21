
def remove_repeat_chars(string):
    # Initialize an empty list to store the characters
    chars = []

    # Iterate through each character in the string
    for char in string:
        # If the character is not already in the list
        if char not in chars:
            # Add the character to the list
            chars.append(char)

    # Initialize an empty string to store the altered string
    altered_string = ""

    # Iterate through each character in the list of unique characters
    for char in chars:
        # If the character is not in the original string
        if char not in string:
            # Add the character to the altered string
            altered_string += char

    return altered_string
