
def filter_chars(s):
    removed_chars = [c for c in s[2:7] if '-' < c < 'L']
    for c in removed_chars:
        s = s.replace(c, '')
    return s
