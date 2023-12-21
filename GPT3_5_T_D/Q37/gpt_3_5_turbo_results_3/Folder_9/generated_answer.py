
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (38 <= i <= 99 and 'A' <= c <= 'Q'))
