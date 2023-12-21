
def filter_chars(s):
    chars_to_remove = set([c for c in s[28:66] if 'O' <= c <= 'd'])
    return ''.join([c for c in s if c not in chars_to_remove])
