
def remove_repeat_chars(s):
    # Create a new string with the repeated characters removed
    new_str = ""
    for i in range(len(s)):
        if s[i] not in new_str:
            new_str += s[i]
    return new_str
