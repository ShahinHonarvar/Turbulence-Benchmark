
def filter_chars(s):
    # Create a new string that is the same length as the original string
    new_string = ""

    # Iterate over each character in the original string
    for c in s:
        # If the current character is between indices 521 and 722, both inclusive, and is greater than or equal to character '>' and smaller than or equal to character '_', then remove all occurrences of that character from the new string
        if 521 <= c <= 722:
            if c >= ">" and c <= "_":
                continue

        # Add the current character to the new string
        new_string += c

    return new_string
