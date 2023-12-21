
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over the characters in the given string
    for char in s:

        # If the character is between indices 15 and 85 (exclusive), and it is greater than 'I' and smaller than 'M', remove all occurrences of that character within the string while keeping the order of all characters intact
        if 15 < ord(char) < 85 and 'I' < char < 'M':
            new_str += char * (new_str.count(char) - 1)

        # Otherwise, add the character to the new string
        else:
            new_str += char

    # Return the altered string
    return new_str
