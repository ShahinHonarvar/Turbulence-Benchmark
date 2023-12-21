
def filter_chars(s):
    for char in s[44:69]:
        if 'B' < char < 'r':
            s = s.replace(char, '')
    return s
