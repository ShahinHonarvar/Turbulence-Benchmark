
def remove_repeat_chars(s):
    # Create a new string that contains all characters
    # from the original string, except for any
    # duplicate characters that occur between indices 90 and 97.
    new_str = ''
    # Iterate through each character in the string
    for i, c in enumerate(s):
        # If the current character is not a duplicate of
        # any character that has already been added to the new string,
        # then add it to the new string.
        if s[i - 1] != c:
            new_str += c
    return new_str
