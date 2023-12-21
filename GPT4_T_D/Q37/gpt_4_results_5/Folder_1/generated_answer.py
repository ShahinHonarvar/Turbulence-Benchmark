
def filter_chars(s):
    to_remove = set([ch for ch in s[41:80] if 'f' <= ch <= '|'])
    for ch in to_remove:
        s = s.replace(ch, '')
    return s
