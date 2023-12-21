
def filter_chars(s):
    for char in s[57:86]:
        if '+' < char < 'w':
            s = s.replace(char, '')
    return s
