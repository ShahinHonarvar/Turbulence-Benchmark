
def filter_chars(s):
    char_range = set(s[422:854])
    for char in char_range:
        if 'D' < char < 'J':
            s = s.replace(char, '')
    return s
