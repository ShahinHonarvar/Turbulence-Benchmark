
def filter_chars(s):
    for char in s[310:591]:
        if 'S' < char < 'm':
            s = s.replace(char, '')
    return s
