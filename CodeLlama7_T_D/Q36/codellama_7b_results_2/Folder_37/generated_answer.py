
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over the characters in the original string
    for c in s:

        # If the character is within the specified range and not equal to '/', add it to the filtered string
        if 44 < ord(c) < 59 and c != "/":
            filtered += c

    # Return the filtered string
    return filtered
