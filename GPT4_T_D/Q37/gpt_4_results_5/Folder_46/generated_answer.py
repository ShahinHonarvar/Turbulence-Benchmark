
def filter_chars(s):
    for char in set(s[11:73]):
        if 'i' <= char <= 'v':
            s = s.replace(char, '')
    return s
