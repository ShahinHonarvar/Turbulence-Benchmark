
def remove_repeat_chars(string):
    # Create a new string with the characters removed
    new_string = ""

    # Iterate over each character in the given string
    for char in string:

        # Check if the current character is already present in the new string
        if char not in new_string:

            # If it's not present, add it to the new string
            new_string += char

    # Return the altered string
    return new_string
