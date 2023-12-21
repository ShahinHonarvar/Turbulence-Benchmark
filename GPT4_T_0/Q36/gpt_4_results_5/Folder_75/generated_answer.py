
def filter_chars(s):
    for char in s[47:74]:
        if '&' < char < 'M':
            s = s.replace(char, '')
    return s
