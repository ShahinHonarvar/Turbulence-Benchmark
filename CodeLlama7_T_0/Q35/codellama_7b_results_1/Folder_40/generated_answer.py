
def remove_repeat_chars(s):
    # Create a new string with the characters of the original string in order
    new_str = ""

    # Iterate over each character in the original string
    for char in s:

        # If the current character is not already in the new string, add it to the end of the new string
        if char not in new_str:
            new_str += char

    # Return the altered string
    return new_str
