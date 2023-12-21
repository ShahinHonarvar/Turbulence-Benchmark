
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if not (31 <= i <= 38) or not (';' <= char <= 'g')])
