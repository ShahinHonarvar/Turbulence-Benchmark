
def filter_chars(string):
    return ''.join(c for i, c in enumerate(string) if not (513 <= i <= 877 and '?' <= c <= 'n'))
