
def filter_chars(s):
    for char in s[71:74]:
        if 'A' < char < 'U':
            s = s.replace(char, '')
    return s
