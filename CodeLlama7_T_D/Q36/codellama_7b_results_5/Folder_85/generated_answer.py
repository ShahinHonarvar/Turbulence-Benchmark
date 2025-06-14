
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ''

    # Iterate through each character in the given string
    for char in s:

        # If the current character is between 55 and 80 (exclusive) and is not 's' or 'S', add it to the new string
        if 55 < ord(char) < 80 and char != 's' and char != 'S':
            new_str += char

    # Return the altered string
    return new_str
