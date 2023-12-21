
def filter_chars(s):
    for char in s[45:48]:
        if '+' < char < 'l':
            s = s.replace(char, '')
    return s
