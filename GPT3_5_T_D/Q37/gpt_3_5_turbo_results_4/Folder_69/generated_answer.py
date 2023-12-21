
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (114 <= i <= 639 and '!' <= c <= 'x'))
