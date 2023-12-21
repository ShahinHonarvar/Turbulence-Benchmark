
def filter_chars(s):
    # Create a new string buffer to store the filtered characters
    buf = []

    # Iterate over each character in the input string
    for c in s:
        # Check if the current character is between indices 12 and 25, both inclusive
        # And if it satisfies the other conditions
        if 12 <= s.index(c) <= 25 and c >= 'P' and c <= 'x':
            # If so, remove all occurrences of this character from the input string
            s = s.replace(c, '')

    # Return the filtered string
    return s
