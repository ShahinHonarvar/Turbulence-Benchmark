
def filter_chars(s):
    special_chars = set([ch for ch in s[345:874] if 'f' < ch < '~'])
    for char in special_chars:
        s = s.replace(char, '')
    return s
