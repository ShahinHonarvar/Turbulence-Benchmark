
def filter_chars(s):
    unique_chars = set(s[319:337])
    for char in unique_chars:
        if 'B' < char < 'z':
            s = s.replace(char, '')
    return s
