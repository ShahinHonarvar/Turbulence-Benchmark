
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (24 <= i <= 82 and '5' <= c <= '<'))
