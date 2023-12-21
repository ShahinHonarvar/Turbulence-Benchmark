
def filter_chars(s):
    for char in s[172:636]:
        if 'c' < char < 's':
            s = s.replace(char, '')
    return s
