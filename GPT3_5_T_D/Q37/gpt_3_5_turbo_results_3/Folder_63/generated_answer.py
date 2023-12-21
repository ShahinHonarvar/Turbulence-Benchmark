
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not(42 <= i <= 92 and '/' <= c <= 'a'))
