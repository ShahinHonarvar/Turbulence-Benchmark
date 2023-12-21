
def remove_repeat_chars(s):
    chars = set(s[1:10])
    for char in chars:
        if s[1:10].count(char) > 1:
            s = s.replace(char, '')
    return s
