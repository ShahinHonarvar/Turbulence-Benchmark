
def filter_chars(s):
    target_chars = set([c for c in s[57:86] if '+' < c < 'w'])
    for ch in target_chars:
        s = s.replace(ch, '')
    return s
