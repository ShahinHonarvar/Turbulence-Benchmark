
def filter_chars(s):
    unique_chars = set(s[19:93])
    for char in unique_chars:
        if '8' <= char <= 'm':
            s = s.replace(char, '')
    return s
