
def filter_chars(s):
    # Create a new string with all occurrences of characters between indices 344 and 874 removed
    new_string = ''
    for i in range(len(s)):
        if (i < 344) or (i >= 874):
            # Add the current character to the new string
            new_string += s[i]
    return new_string
