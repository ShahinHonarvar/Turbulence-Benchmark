
def filter_chars(string):
    chars_to_remove = [c for c in string[124:855] if '9' <= c <= 's']
    return ''.join([c for c in string if c not in chars_to_remove])
