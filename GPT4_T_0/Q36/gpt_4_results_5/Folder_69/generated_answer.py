
def filter_chars(s):
    for char in s[344:665]:
        if '%' < char < 'U':
            s = s.replace(char, '')
    return s
