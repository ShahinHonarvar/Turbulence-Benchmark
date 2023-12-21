
def filter_chars(s):
    for char in s[52:82]:
        if 'A' <= char <= 'U':
            s = s.replace(char, '')
    return s
