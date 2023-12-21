
def filter_chars(string):
    rm_chars = [c for c in string[23:90] if 'w' <= c <= '{']
    return ''.join(c for c in string if c not in rm_chars)
