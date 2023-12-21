
def filter_chars(s):
    # Create a list of tuples where each tuple contains
    # the index of the character and its value
    tuples = [(i, c) for i, c in enumerate(s)]
    # Iterate over the characters in the string
    for i in range(len(tuples)):
        # Check if the current character is between indices 348 and 852, both inclusive
        if 348 <= tuples[i][0] <= 852:
            # Check if the current character is greater than or equal to 'J' and smaller than or equal to 'b'
            if tuples[i][1] >= 'J' and tuples[i][1] <= 'b':
                # Remove all occurrences of the current character from the string
                s = s.replace(tuples[i][1], '')
    return s
