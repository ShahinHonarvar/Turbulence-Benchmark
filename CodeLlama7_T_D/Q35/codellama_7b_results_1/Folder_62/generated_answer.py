
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 50 and 92, exclusive
    new_str = ""
    for i in range(len(s)):
        if s[i] not in s[50:92]:
            new_str += s[i]
    return new_str
