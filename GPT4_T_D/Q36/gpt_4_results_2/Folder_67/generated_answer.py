
def filter_chars(s):
    for ch in s[19:31]:
        if 'H' < ch < '|':
            s = s.replace(ch, '')
    return s
