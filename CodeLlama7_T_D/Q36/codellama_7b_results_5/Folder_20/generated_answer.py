
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ''

    # Iterate through each character in the string
    for char in s:

        # If the character is between the indices 13 and 40 (both exclusive)
        # and if it is greater than ':' and smaller than 'C'
        # then remove all occurrences of that character from the string
        if (13 < len(s) < 40) and (char > ':') and (char < 'C'):
            new_str += char * 0

    return new_str
