
def filter_chars(s):
    # Create a new string with all characters removed
    # that are between 283 and 484 (both exclusive)
    filtered = ""

    # Iterate over each character in the original string

    for c in s:
        # If the current character is not between 283 and 484,

        if ord(c) < 283 or ord(c) > 484:
            filtered += c

    return filtered
