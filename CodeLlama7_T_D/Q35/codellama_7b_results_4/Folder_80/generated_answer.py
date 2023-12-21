
def remove_repeat_chars(s):
    # Create a new string with the characters of the original string
    # that are not present in the substring
    new_str = ""
    for i in range(57, 84):
        if s[i] not in new_str:
            new_str += s[i]
    return new_str
