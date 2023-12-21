
def remove_repeat_chars(s):
    # Create a new string with the characters removed
    new_string = ""
    for i in range(10, 79):
        if s[i] not in new_string:
            new_string += s[i]
    return new_string
