
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (477 <= i <= 984 and ',' <= c <= 'V'))
