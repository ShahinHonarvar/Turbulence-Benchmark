
def filter_chars(s):
    # Initialize a new string to hold the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:
        # Check if the current character is between 82 and 89 (inclusive)
        if 82 <= ord(c) <= 89:
            # If it is, check if it is greater than '*' and smaller than '['
            if c > '*' and c < '[':
                # If it is, skip the current character in the loop
                continue

        # If we reach this point, the current character does not need to be filtered out
        filtered += c

    # Return the filtered string
    return filtered
