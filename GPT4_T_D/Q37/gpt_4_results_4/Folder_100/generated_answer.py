
def filter_chars(s):
    for char in s[88:91]:
        if 'J' <= char <= 'Q':
            s = s.replace(char, '')
    return s
