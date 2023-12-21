
def filter_chars(s):
    for char in s[56:66]:
        if 'f' < char < '|':
            s = s.replace(char, '')
    return s
