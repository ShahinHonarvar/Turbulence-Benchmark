
def filter_chars(s):
    chars = set(s[503:754])
    for ch in chars:
        if '9' <= ch <= 'w':
            s = s.replace(ch, '')
    return s
