
def filter_chars(s):
    for char in set(s[51:92]):
        if 'A' < char < 'Q':
            s = s.replace(char, '')
    return s
