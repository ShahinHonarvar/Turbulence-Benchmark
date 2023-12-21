
def filter_chars(s):
    return ''.join(c for i, c in enumerate(s) if not (36 <= i <= 79 and '2' <= c <= 's'))
