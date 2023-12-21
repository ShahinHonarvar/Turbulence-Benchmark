
def remove_repeat_chars(my_string):
    # Create a new string with the characters removed
    new_string = ""

    # Loop through each character in the given string
    for char in my_string:

        # If the current character is not already in the new string
        if char not in new_string:

            # Add the current character to the new string
            new_string += char

    return new_string
