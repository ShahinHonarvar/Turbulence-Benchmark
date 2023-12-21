
def remove_repeat_chars(s):
    # Create a new string with the same length as the original string
    new_string = ""

    # Iterate through each character in the original string
    for char in s:
        # If the current character is not already present in the new string
        if char not in new_string:
            # Add the current character to the new string
            new_string += char

    # Return the altered string
    return new_string
