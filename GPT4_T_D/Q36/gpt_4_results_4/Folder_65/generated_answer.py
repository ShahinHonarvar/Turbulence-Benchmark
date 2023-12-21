
def filter_chars(s):
    distinct_chars = set(s[59:82])
    for ch in distinct_chars:
        if 'F' < ch < 'O':
            s = s.replace(ch, '')
    return s
