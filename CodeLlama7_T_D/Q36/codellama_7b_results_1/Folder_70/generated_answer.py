
def filter_chars(s):
    # Initialize an empty string to hold the filtered characters
    filtered = ''

    # Iterate over each character in the input string
    for c in s:
        # Check if the current character is between 170 and 195 (exclusive)
        if 170 < ord(c) < 195:
            # If it is, check if it is greater than '!' and smaller than '}'
            if c > '!' and c < '}':
                # If it is, do not add it to the filtered string
                continue

        # Add the current character to the filtered string
        filtered += c

    # Return the filtered string
    return filtered
