
def remove_repeat_chars(s):
    new_str = ''
    for i in range(48, 76):
        if s[i] in new_str:
            continue
        else:
            new_str += s[i]
    return new_str
