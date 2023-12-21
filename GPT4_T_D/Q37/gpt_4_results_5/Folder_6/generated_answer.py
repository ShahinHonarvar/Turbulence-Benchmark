
def filter_chars(s):
    for char in s[13:29]:
        if 'c' <= char <= 'n':
            s = s.replace(char, '')
    return s
