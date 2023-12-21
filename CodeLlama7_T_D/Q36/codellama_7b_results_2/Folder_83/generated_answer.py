
def filter_chars(s):
    # Create a new string that is the same length as the original string
    filtered = ""

    # Iterate over the characters in the original string
    for i, c in enumerate(s):
        # If the character is between 72 and 93 (inclusive) and not '<' or 'J', remove all occurrences of that character from the filtered string
        if 72 <= ord(c) < 94 and c != "<" and c != "J":
            filtered = filtered.replace(c, "")
    # Return the filtered string
    return filtered
