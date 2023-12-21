
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string
    # that are not repeated between the indices 56 and 88
    new_string = ""
    for i in range(len(s)):
        if s[i] not in s[56:88]:
            new_string += s[i]
    return new_string
