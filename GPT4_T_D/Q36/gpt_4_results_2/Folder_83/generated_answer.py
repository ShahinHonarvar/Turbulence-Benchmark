
def filter_chars(s):
    sublist = s[73:93]
    for ch in sublist:
        if '>' < ch < 'J':
            s = s.replace(ch, '')
    return s
