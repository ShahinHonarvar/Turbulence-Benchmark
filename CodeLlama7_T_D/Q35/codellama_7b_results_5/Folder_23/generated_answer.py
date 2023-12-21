
def remove_repeat_chars(s):
    # Create a new string with the characters in the original string that do not occur more than once between the indices 20 and 36, both exclusive
    new_string = ""
    for i in range(len(s)):
        if s[i] not in s[20:36]:
            new_string += s[i]
    return new_string
