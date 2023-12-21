
def filter_chars(s):
    for char in s[422:854]:
        if 'D' < char < 'J':
            s = s.replace(char, '')
    return s
