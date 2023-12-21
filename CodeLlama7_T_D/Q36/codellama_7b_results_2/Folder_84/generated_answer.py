
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ''

    # Iterate over each character in the input string
    for c in s:
        # If the character is between indices 171 and 636 (exclusive),
        # and it is greater than 'c' and smaller than 's',
        # then remove all occurrences of that character from the filtered string
        if 171 < c.lower() < 636:
            filtered = filtered.replace(c, '')

    return filtered
