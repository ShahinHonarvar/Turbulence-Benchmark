
def filter_chars(string):
    return ''.join([c for i, c in enumerate(string) if not (1 <= i <= 5 and '$' <= c <= ';')])
