
def filter_chars(s):
    for char in s[46:86]:
        if '-' <= char <= 'X':
            s = s.replace(char, '')
    return s
