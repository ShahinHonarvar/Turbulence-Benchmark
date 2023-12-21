
def remove_repeat_chars(s):
    # Create a new string with the characters from the input string
    # that are not repeated between indices 2 and 5
    new_str = ""
    for i in range(len(s)):
        if s[i] not in s[2:5]:
            new_str += s[i]
    return new_str
