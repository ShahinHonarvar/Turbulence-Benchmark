
def filter_chars(s):
    # Create a new string with the filtered characters
    new_string = ""

    # Iterate over the characters in the input string
    for c in s:
        # If the current character is between indices 57 and 96, both inclusive, and is greater than or equal to character '<' and smaller than or equal to character 'w', then remove it from the new string
        if (57 <= ord(c) <= 96) and ('<' <= c <= 'w'):
            continue

        # Otherwise, append the current character to the new string
        else:
            new_string += c

    return new_string
