
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_string = ""

    # Iterate through each character in the original string
    for char in s:

        # Check if the current character is already in the new string
        if char not in new_string:

            # If it's not, add it to the new string
            new_string += char

    return new_string
