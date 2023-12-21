
def filter_chars(s):
    for char in s[477:985]:
        if ',' <= char <= 'V':
            s = s.replace(char, '')
    return s
