
def filter_chars(s):
    for char in s[155:222]:
        if 'A' < char < 'f':
            s = s.replace(char, '')
    return s
