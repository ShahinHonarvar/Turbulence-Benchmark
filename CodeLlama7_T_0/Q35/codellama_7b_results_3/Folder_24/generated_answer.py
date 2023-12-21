
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the character is not repeated between indices 13 and 91, inclusive
        if s.count(char) == 1:

            # Add the character to the new string
            new_str += char

    # Return the altered string
    return new_str
