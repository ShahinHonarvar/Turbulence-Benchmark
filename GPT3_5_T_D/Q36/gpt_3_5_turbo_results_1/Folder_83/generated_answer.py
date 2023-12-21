
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (72 <= i < 93 and '<' < c < 'J'))
