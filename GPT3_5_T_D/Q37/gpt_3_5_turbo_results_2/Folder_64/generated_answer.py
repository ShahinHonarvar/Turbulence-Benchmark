
def filter_chars(string):
    return ''.join([c for c in string if c <= 'L' or c > 'a' or (c > 'G' and c < 'b')])
