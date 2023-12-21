
def filter_chars(s):
    for char in s[225:382]:
        if 'D' <= char <= 'Y':
            s = s.replace(char, '')
    return s
