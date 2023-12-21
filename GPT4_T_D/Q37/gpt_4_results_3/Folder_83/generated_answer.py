
def filter_chars(input_str):
    range_chars = set([c for c in input_str[29:80] if 'K' <= c <= 'z'])
    return ''.join([c for c in input_str if c not in range_chars])
