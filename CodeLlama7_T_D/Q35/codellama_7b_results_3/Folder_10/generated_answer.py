
def remove_repeat_chars(s):
    # Initialize a new string
    new_str = ""
    # Iterate through the characters of the given string
    for char in s:
        # If the current character is not already in the new string
        if char not in new_str:
            # Add the current character to the new string
            new_str += char
    return new_str
