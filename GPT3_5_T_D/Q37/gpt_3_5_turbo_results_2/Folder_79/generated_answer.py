
def filter_chars(string):
    return ''.join(ch for i, ch in enumerate(string) if not (10 <= i <= 52 and '@' <= ch <= 'T'))
