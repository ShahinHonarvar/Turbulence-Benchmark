
def remove_repeat_chars(s):
    # Create a new string without the repeated characters
    new_str = ""
    for i in range(17, 88):
        if s[i] not in new_str:
            new_str += s[i]
    return new_str
