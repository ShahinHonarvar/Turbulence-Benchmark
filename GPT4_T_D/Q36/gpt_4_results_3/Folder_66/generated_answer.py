
def filter_chars(s):
    unique_chars = set(s[40:87])
    for char in unique_chars:
        if '!' < char < '}':
            s = s.replace(char, '')
    return s
