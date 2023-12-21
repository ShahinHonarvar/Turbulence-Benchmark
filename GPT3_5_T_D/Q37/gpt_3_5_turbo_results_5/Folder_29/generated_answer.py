
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if 12 <= i <= 88 and '&' <= c <= 'v'])
