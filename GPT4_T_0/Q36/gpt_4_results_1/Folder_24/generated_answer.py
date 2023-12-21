
def filter_chars(s):
    for char in s[11:15]:
        if 't' < char < 'v':
            s = s.replace(char, '')
    return s
