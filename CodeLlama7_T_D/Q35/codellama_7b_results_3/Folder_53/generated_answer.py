
def remove_repeat_chars(string):
    # Create a new string with the characters in order
    new_string = ""

    # Iterate over each character in the string
    for char in string:
        # If the character is not already in the new string, add it
        if char not in new_string:
            new_string += char

    # Return the altered string
    return new_string
