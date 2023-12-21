
def filter_chars(s):
    for char in s[43:68]:
        if 't' < char < 'x':
            s = s.replace(char, '')
    return s
