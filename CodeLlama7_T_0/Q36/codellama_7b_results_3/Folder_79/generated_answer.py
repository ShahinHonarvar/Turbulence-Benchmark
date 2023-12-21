
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between the indices 11 and 46 (both exclusive)
        if 11 < ord(char) < 46:
            # And it is greater than character '!' and smaller than character 'A'
            if ord(char) > ord('!') and ord(char) < ord('A'):
                # Skip this character in the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
