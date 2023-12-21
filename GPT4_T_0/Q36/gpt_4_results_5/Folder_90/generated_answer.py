
def filter_chars(s):
    for char in s[345:874]:
        if 'f' < char < '~':
            s = s.replace(char, '')
    return s
