
def remove_repeat_chars(s):
    # Create a new string with all characters removed
    new_string = ""

    # Iterate over each character in the given string
    for char in s:
        # If the current character is not already in the new string, add it
        if char not in new_string:
            new_string += char

    # Return the altered string
    return new_string
