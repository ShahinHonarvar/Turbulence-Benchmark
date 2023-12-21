
def filter_chars(s):
    set_chars = set([ch for ch in s[222:419] if ch > '-' and ch < 'v'])
    for ch in set_chars:
        s = s.replace(ch, '')
    return s
