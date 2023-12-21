
def filter_chars(s):
    to_remove = [c for c in s[47:74] if '&' < c < 'M']
    for rem in set(to_remove):
        s = s.replace(rem, '')
    return s
