
def remove_repeat_chars(s):
    # Create a new string with the characters of the original string in order
    new_str = ""

    # Iterate over the characters in the original string
    for char in s:

        # If the current character is not already present in the new string
        if char not in new_str:

            # Add the current character to the new string
            new_str += char

    # Return the altered string
    return new_str
