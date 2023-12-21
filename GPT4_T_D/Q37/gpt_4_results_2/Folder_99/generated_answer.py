
def filter_chars(s):
    chars = s[373:902]
    for char in chars:
        if 'T' <= char <= 'h':
            s = s.replace(char, '')
    return s
