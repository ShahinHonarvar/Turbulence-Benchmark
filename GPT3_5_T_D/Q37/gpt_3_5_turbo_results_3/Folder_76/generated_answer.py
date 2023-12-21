
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not(379 <= i <= 898 and 'M' <= c <= 'v'))
