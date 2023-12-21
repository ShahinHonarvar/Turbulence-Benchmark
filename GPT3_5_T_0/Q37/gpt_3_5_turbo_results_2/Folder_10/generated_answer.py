
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 63 or i > 84 or char < 'E' or char > '~'])
