
def filter_chars(s):
    for char in s[2:4]:
        if '5' <= char <= '_':
            s = s.replace(char, '')
    return s
