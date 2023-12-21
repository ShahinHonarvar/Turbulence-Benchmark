
def remove_repeat_chars(s):
    for i in range(36, 52):
        char = s[i]
        if s.count(char) > 1:
            s = s.replace(char, '')
    return s
