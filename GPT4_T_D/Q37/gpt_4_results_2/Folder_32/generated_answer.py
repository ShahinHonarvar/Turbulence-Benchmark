
def filter_chars(s):
    restricted = set([char for char in s[23:90] if 'w' <= char <= '{'])
    return ''.join([char for char in s if char not in restricted])
