
def filter_chars(s):
    reduced_chars = [c for c in s[25:37] if 'A' < c < 'h']
    for char in reduced_chars:
        s = s.replace(char, '')
    return s
