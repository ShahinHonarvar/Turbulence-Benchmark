
def filter_chars(s):
    for char in s[32:73]:
        if 'M' < char < 'j':
            s = s.replace(char, '')
    return s
