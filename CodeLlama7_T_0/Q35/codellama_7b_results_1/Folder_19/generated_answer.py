
def remove_repeat_chars(s):
    # Create a new string with the characters from the original string that are not repeated between indices 1 and 4, exclusive
    new_string = ""
    for i in range(len(s)):
        if s[i] not in s[1:4]:
            new_string += s[i]
    return new_string
