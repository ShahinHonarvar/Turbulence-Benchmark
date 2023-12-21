
def filter_chars(string):
    return ''.join([char for idx, char in enumerate(string) if idx < 35 or idx > 89 or not ('E' <= char <= 't')])
