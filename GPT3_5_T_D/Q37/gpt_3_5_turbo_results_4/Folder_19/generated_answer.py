
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (35 <= i <= 89 and 'E' <= c <= 't'))
