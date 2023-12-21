
def filter_chars(string):
    return ''.join([ch for i, ch in enumerate(string) if i < 71 or i > 94 or not ('K' <= ch <= 'a')])
