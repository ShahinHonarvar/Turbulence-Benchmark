
def filter_chars(s):
    filter_chars = set([char for char in s[41:65] if 'K' <= char <= ']'])
    for char in filter_chars:
        s = s.replace(char, '')
    return s
