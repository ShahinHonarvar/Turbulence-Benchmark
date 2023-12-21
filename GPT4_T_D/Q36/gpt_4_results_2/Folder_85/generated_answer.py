
def filter_chars(s):
    filter_chars = [c for c in s[56:80] if 'S' < c < 's']
    for char in filter_chars:
        s = s.replace(char, '')
    return s
