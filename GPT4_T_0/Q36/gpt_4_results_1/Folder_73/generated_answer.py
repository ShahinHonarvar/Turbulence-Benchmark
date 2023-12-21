
def filter_chars(s):
    for char in s[67:90]:
        if '#' < char < 'T':
            s = s.replace(char, '')
    return s
