
def filter_chars(s):
    chars_to_remove = set([c for c in s[33:71] if '7' <= c <= 'k'])
    return ''.join([c for c in s if c not in chars_to_remove]) 
