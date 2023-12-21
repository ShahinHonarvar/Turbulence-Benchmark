
def filter_chars(s):
    for char in s[0:2]:
        if '*' <= char <= 's':
            s = s.replace(char, '')
    return s
