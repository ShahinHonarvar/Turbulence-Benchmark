
def filter_chars(s):
    for char in s[62:88]:
        if '%' < char < 'q':
            s = s.replace(char, '')
    return s
