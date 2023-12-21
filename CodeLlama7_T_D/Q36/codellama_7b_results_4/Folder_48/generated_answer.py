
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""
    # Iterate over the characters in the original string
    for i, c in enumerate(s):
        # If the character is between 'A' and 'f', exclude it from the new string
        if ord('A') <= ord(c) <= ord('f'):
            continue

        # Otherwise, add the character to the new string
        new_str += c

    return new_str
