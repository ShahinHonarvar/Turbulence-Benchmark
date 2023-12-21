
def filter_chars(s):
    for char in s[32:70]:
        if 'B' < char < 'v':
            s = s.replace(char, '')
    return s
