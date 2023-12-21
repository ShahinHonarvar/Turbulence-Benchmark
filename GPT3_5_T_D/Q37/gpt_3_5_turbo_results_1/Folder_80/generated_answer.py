
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if (36 <= i <= 79) and ('a' <= c <= 'i'))
