
def filter_chars(s):
    for char in s[72:95]:
        if '.' <= char <= 'b':
            s = s.replace(char, '')
    return s
