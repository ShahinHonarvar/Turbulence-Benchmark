
def filter_chars(s):
    chars_to_remove = set([c for c in s[29:98] if '-' <= c <= 'n'])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
