
def filter_chars(s):
    chars_to_remove = [c for c in s[2:4] if '5' <= c <= '_']
    return ''.join([c for c in s if c not in chars_to_remove])
