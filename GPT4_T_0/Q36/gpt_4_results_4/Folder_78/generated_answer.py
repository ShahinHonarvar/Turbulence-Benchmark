
def filter_chars(s):
    for char in s[30:33]:
        if '%' < char < 'a':
            s = s.replace(char, '')
    return s
