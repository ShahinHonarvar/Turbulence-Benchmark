
def remove_repeat_chars(s):
    # Create a new string with the characters from s
    # that occur once between indices 1 and 8, exclusive
    new_str = ""

    # Iterate over the characters in s
    for c in s:

        # If the character occurs only once in the substring
        # between indices 1 and 8, exclusive
        if s.count(c) == 1:
            # Add the character to the new string
            new_str += c

    # Return the altered string
    return new_str
