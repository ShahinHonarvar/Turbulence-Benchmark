
def remove_repeat_chars(s):
    # Create a new string with the characters of the original string in order
    new_str = ""

    # Iterate over the characters in the original string
    for char in s:

        # If the character is not already in the new string, append it
        if char not in new_str:
            new_str += char

    return new_str
