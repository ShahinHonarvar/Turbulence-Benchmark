
def filter_chars(s):
    char_set = set([c for c in s[2:7] if '?' <= c <= 'f'])
    for c in char_set:
        s = s.replace(c, '')
    return s
