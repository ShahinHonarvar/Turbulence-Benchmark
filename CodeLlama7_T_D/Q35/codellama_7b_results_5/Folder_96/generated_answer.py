
def remove_repeat_chars(string):
    # Create a new string with all characters from the original string
    new_string = ''

    # Iterate over each character in the original string
    for char in string:
        # If the current character is not already in the new string
        if char not in new_string:
            # Add the character to the new string
            new_string += char

    # Return the altered string
    return new_string
