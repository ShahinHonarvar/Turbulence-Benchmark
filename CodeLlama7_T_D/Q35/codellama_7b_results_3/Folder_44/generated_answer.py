
def remove_repeat_chars(string):
    # Create a new string with the desired characters removed
    new_string = ''
    # Iterate through each character in the given string
    for char in string:
        # If the current character is not in the desired range (36, 52)
        if ord(char) < 36 or ord(char) > 52:
            # Add the current character to the new string
            new_string += char

    return new_string
