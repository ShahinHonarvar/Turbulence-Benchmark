
def remove_repeat_chars(s):
    new_string = ''
    for i in range(len(s)):
        if s[i] not in new_string:
            new_string += s[i]
    return new_string
