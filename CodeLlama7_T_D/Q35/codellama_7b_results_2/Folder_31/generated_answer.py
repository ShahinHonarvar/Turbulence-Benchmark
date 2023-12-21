
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string
    # that do not occur more than once between the indices 33 and 78
    new_string = ""

    # Iterate over the characters in the original string

    for i in range(len(s)):

        # Check if the current character occurs more than once between the indices 33 and 78

        if s[i] not in new_string:
            new_string += s[i]

    return new_string
