
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over each character in the given string
    for char in s:
        # If the current character is between indices 34 and 67, both inclusive, and is greater than or equal to character 'W' and smaller than or equal to character 'x', then remove all occurrences of that character from the new string
        if (34 <= char <= 67) and ('W' <= char <= 'x'):
            continue

        # Otherwise, add the current character to the new string
        else:
            new_str += char

    # Return the altered string
    return new_str
