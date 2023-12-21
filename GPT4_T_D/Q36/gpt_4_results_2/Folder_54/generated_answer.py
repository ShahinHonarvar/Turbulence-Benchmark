
def filter_chars(s):
    filtered_chars = set([c for c in s[19:38] if ')' < c < 'P'])
    for char in filtered_chars:
        s = s.replace(char, '')
    return s
