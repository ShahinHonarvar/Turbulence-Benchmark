
def filter_chars(s):
    for char in s[27:86]:
        if '!' <= char <= 'B':
            s = s.replace(char, '')
    return s
