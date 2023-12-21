
def remove_repeat_chars(string):
    # Create a new string with the characters removed
    new_string = ""

    # Iterate through each character in the given string
    for char in string:
        # If the current character is not already present in the new string
        if char not in new_string:
            # Add the current character to the new string
            new_string += char

    # Return the altered string
    return new_string
