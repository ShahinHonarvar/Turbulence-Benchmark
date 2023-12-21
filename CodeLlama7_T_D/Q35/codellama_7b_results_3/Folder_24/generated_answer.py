
def remove_repeat_chars(s):
    # Create a new string with no repeated characters
    new_str = ""

    # Iterate over each character in the original string
    for char in s:

        # If the current character is not already in the new string, add it
        if char not in new_str:
            new_str += char

    # Return the altered string
    return new_str
