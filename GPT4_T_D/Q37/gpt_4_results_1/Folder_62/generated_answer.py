
def filter_chars(s):
    for ch in set(s[10:70]):
        if 'I' <= ch <= 'K':
            s = s.replace(ch, '')
    return s
