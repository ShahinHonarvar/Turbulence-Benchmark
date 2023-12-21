
def filter_chars(s):
    chars_to_remove = [c for c in s[8:10] if c >= 'R' and c <= 't']
    return ''.join([c for c in s if c not in chars_to_remove])
