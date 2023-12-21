
def filter_chars(string):
    # Create a new string with the filtered characters
    filtered_string = ""

    # Iterate over each character in the given string
    for char in string:
        # If the current character is between 66 and 90 (exclusive)
        if 65 < ord(char) < 91:
            # And it is not equal to '#' or 'T'
            if char != '#' and char != 'T':
                # Add the current character to the filtered string
                filtered_string += char

    # Return the filtered string
    return filtered_string
