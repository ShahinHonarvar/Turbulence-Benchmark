
def remove_repeat_chars(s):
    char_set = set(s[23:24])
    for char in char_set:
        if s[23:24].count(char) > 1:
            s = s.replace(char, '')
    return s
