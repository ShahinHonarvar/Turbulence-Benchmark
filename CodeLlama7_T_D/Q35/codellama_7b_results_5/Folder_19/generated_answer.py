
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate over each character in the string
    for i, c in enumerate(s):

        # If the current character is not repeated between indices 1 and 4, inclusive
        if s.count(c) == 1 or i < 1 or i > 4:

            # Add the character to the new string
            new_str += c

    return new_str
