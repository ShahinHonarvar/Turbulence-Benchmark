
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between indices 69 and 87 (both exclusive)
        if 69 < ord(char) < 87:
            # And it is greater than '#' and smaller than 'L'
            if ord(char) > ord('#') and ord(char) < ord('L'):
                # Skip this character in the filtered string
                continue

        # Add the current character to the filtered string
        filtered_string += char

    # Return the filtered string
    return filtered_string
