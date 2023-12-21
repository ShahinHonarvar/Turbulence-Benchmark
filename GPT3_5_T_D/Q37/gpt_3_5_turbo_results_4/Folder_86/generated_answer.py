
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if i < 164 or i > 706 or c < 'O' or c > '}'])
