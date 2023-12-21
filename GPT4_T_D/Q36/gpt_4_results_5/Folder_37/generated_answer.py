
def filter_chars(s):
    substr = s[45:59]
    for ch in substr:
        if '/' < ch < '6':
            s = s.replace(ch, '')
    return s
