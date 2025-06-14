
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over the characters in the original string
    for c in s:

        # If the current character is between indices 54 and 83, both inclusive, and is greater than or equal to character 'j' and smaller than or equal to character 'v', then remove it from the new string
        if (54 <= s.index(c) <= 83) and ('j' <= c <= 'v'):
            continue

        # Otherwise, append the current character to the new string
        else:
            new_str += c

    # Return the filtered string
    return new_str
