
def filter_chars(s):
    unique_chars = set(s[44:69])
    for char in unique_chars:
        if 'B' < char < 'r':
            s = s.replace(char, '')
    return s
