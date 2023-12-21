
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if i < 86 or i >= 93 or c <= 'E' or c >= '~')
