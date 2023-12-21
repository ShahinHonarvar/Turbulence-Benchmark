
def remove_repeat_chars(s):
    # Create a new string with the characters from the given string that do not occur more than once between the indices 86 and 90, both exclusive
    new_string = ""
    for i in range(len(s)):
        if s[i] not in s[86:90]:
            new_string += s[i]
    return new_string
