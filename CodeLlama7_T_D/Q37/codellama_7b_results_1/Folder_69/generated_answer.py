
def filter_chars(s):
    # Initialize an empty string to hold the filtered characters
    filtered = ""

    # Iterate over the characters in the input string
    for c in s:

        # If the current character is between indices 114 and 639, inclusive, and it is greater than or equal to '!' and smaller than or equal to 'x', then add it to the filtered string
        if (114 <= ord(c) <= 639) and ('!' <= c <= 'x'):
            filtered += c

    # Return the filtered string
    return filtered
