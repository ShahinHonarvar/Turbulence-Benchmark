
def remove_repeat_chars(s):
    new_string = ''
    for i in range(68, 99):
        if s[i] not in new_string:
            new_string += s[i]
    return new_string
