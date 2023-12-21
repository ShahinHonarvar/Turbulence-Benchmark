
def filter_chars(s):
    # Create a new string with the filtered characters
    filtered = ""

    # Iterate over the characters in the original string
    for c in s:
        # If the character is between indices 52 and 81, both inclusive, and is greater than or equal to character 'A' and smaller than or equal to character 'U', then remove all occurrences of that character from the filtered string
        if (52 <= ord(c) <= 81) and ('A' <= c <= 'U'):
            filtered = filtered.replace(c, "")

    # Return the altered string
    return filtered
