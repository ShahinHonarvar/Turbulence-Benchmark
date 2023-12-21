
def remove_repeat_chars(s):
    part = s[49:76]
    for char in set(part):
        if part.count(char) > 1:
            s = s.replace(char, '')
    return s
