
def filter_chars(s):
    chars_to_remove = set([c for c in s[20:80] if '!' <= c <= 'T'])
    return ''.join([c for c in s if c not in chars_to_remove])
