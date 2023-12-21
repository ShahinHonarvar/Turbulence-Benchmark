
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 330 and 543
    new_str = ""
    for i in range(len(s)):
        if s[i] not in s[330:543]:
            new_str += s[i]
    return new_str
