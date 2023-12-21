
def filter_chars(s):
    for char in s[43:67]:
        if '6' < char < 'g':
            s = s.replace(char, '')
    return s
