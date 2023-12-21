
def filter_chars(s):
    unique_chars = set(s[32:70])
    for char in unique_chars:
        if 'B' < char < 'v':
            s = s.replace(char, '')
    return s
