
def filter_chars(string):
    return ''.join(c for c in string if c <= ',' or c >= 'f')
