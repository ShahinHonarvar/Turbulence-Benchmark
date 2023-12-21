
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (49 <= i < 56 and 'I' < c < 'a'))
