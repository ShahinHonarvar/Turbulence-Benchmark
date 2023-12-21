
def filter_chars(s):
    for char in set(s[11:79]):
        if '?' < char < 'm':
            s = s.replace(char, '')
    return s
