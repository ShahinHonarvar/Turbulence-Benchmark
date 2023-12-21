
def filter_chars(string):
    return ''.join(c for c in string if not ('!' < c < 'B') or c in string[35:60])
