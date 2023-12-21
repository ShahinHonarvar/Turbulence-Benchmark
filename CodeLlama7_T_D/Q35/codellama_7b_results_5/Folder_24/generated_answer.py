
def remove_repeat_chars(s):
    # Create a new string with the same characters as s, but without any repeated characters
    new_string = ""
    for i in range(len(s)):
        if s[i] not in new_string[:i]:
            new_string += s[i]
    return new_string
