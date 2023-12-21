
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if not (71 <= i <= 96 and '_' <= c <= 'o'))
