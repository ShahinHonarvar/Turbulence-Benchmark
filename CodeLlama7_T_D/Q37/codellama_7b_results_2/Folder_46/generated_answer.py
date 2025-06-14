
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:
        # Check if the current character is between indices 11 and 72, both inclusive, and is greater than or equal to 'i' and smaller than or equal to 'v'
        if (len(s) > 11 and len(s) < 73) and ('i' <= c <= 'v'):
            # If the current character meets the criteria, append it to the filtered string
            filtered += c

    # Return the filtered string
    return filtered
