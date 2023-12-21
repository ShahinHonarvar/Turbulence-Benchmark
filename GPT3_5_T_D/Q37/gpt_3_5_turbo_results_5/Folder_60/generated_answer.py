
def filter_chars(string):
    return ''.join([char for index, char in enumerate(string) if 12 <= index <= 77 and ':' <= char <= 'L'])
