
def filter_chars(s):
    chars_to_remove = [i for i in s[41:87] if 'S' <= i <= 's']
    return ''.join([c for c in s if c not in chars_to_remove])
