
def filter_chars(s):
    removed_chars = [c for c in s[11:79] if '?' < c < 'm']
    for ch in removed_chars:
        s = s.replace(ch, '')
    return s
