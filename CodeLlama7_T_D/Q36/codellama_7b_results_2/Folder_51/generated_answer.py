
def filter_chars(s):
    # Initialize an empty string to store the filtered characters
    filtered = ""

    # Iterate over each character in the input string
    for c in s:
        # Check if the current character is between indices 58 and 81 (both exclusive)
        if 57 < ord(c) < 82:
            # If the character is not "5" or ">", keep it in the filtered string
            filtered += c

    # Return the filtered string
    return filtered
