
def filter_chars(string):
    filtered_chars = set(c for c in string[12:89] if '&' <= c <= 'v')
    return ''.join(c for c in string if c not in filtered_chars)
