
def remove_repeat_chars(s):
    # Create a new string with the same characters as s
    new_string = ""

    # Iterate over each character in s
    for char in s:

        # If the current character is not already in the new string
        if char not in new_string:

            # Add the current character to the new string
            new_string += char

    # Return the altered string
    return new_string
