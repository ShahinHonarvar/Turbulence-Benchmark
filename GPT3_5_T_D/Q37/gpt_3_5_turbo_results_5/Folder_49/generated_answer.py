
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if 42 <= i <= 97 and '*' <= c <= 'b')
