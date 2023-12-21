
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ''

    # Iterate over each character in the input string
    for c in s:
        # If the current character is between indices 28 and 65, both inclusive, and is greater than or equal to 'O' and smaller than or equal to 'd', then append it to the filtered string
        if (28 <= ord(c) <= 65) and ('O' <= c <= 'd'):
            filtered += c

    # Return the filtered string

    return filtered
