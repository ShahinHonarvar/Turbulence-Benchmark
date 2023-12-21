
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 26 or 64 < i or c < 'V' or c > 'o'])
