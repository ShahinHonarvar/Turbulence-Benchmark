
def filter_chars(s):
    filter_chars = set([ch for ch in s[4:5] if '7' <= ch <= 'o'])
    for ch in filter_chars:
        s = s.replace(ch, '')
    return s
