
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the character is not already in the new string, add it
        if char not in new_str:
            new_str += char

    # Return the altered string
    return new_str
