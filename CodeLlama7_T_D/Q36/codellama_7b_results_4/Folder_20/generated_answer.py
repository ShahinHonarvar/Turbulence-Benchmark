
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate over each character in the input string
    for char in s:

        # If the current character is between 13 and 40, and it is not ':' or 'C', then add it to the new string
        if (char >= '!' and char <= '@') or (char >= '[' and char <= '`') or (char >= '{' and char <= '~'):
            new_string += char

    # Return the filtered string
    return new_string
