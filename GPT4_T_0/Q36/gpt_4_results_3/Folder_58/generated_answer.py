
def filter_chars(s):
    for char in s[319:337]:
        if 'B' < char < 'z':
            s = s.replace(char, '')
    return s
