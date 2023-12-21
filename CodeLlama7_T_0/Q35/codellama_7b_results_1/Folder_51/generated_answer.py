
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the character is not repeated between indices 6 and 9, add it to the new string
        if s.count(char) == 1:
            new_str += char

    # Return the altered string
    return new_str
