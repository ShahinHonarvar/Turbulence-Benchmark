
def remove_repeat_chars(s):
    # Create a new string with the same length as the original string
    new_string = ""
    # Iterate through each character in the original string
    for i, char in enumerate(s):
        # If the current character is not in the range of 100 to 200, inclusive
        if i < 100 or i > 200:
            # Append the character to the new string
            new_string += char

    # Return the altered string

    return new_string
