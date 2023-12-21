
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 39 and 43, exclusive
    new_string = ""
    for i in range(len(s)):
        if s[i] not in s[39:43]:
            new_string += s[i]
    return new_string
