
def remove_repeat_chars(string):
    # Create a new string with all characters removed
    new_string = ""

    # Iterate through each character in the given string
    for char in string:

        # If the current character is not already in the new string, add it to the end of the new string
        if char not in new_string:
            new_string += char

    # Return the altered string
    return new_string
