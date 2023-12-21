
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 12 or i > 25 or char < 'P' or char > 'x'])
