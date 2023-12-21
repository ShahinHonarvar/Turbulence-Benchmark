
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_str = ""

    # Iterate through each character in the given string
    for char in s:

        # If the current character is not already in the new string, append it
        if char not in new_str:
            new_str += char

    return new_str
