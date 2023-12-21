
def filter_chars(s):
    return ''.join([char for index, char in enumerate(s) if not (20 <= index <= 79 and '!' <= char <= 'T')])
