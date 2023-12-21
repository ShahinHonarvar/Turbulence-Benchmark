
def filter_chars(s):
    chars_to_remove = set([c for c in s[379:899] if 'M' <= c <= 'v'])
    altered_string = ''.join([c for c in s if c not in chars_to_remove])
    return altered_string
