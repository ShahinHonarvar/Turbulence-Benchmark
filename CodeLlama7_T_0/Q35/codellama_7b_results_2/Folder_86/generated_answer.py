
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 19 and 32, exclusive
    new_str = ""
    for i in range(len(s)):
        if s[i] not in s[19:32]:
            new_str += s[i]
    return new_str
