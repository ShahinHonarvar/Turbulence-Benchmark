
def filter_chars(s):
    # Create a new string with the filtered characters
    new_str = ""

    # Iterate over the characters in the original string
    for char in s:

        # If the character is between indices 19 and 32, both inclusive, and is greater than or equal to character 'f' and smaller than or equal to character 'o', then remove it from the new string
        if (19 <= s.index(char) <= 32) and ('f' <= char <= 'o'):
            continue

        # Otherwise, add the character to the new string
        else:
            new_str += char

    # Return the filtered string
    return new_str
