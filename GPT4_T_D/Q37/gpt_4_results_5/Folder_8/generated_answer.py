
def filter_chars(input_string):
    banned_chars = set([c for c in input_string[41:87] if 'S' <= c <= 's'])
    return ''.join(c for c in input_string if c not in banned_chars)
