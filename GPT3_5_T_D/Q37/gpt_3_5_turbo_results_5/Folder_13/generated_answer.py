
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if not (124 <= i <= 854 and '9' <= char <= 's')])
