
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 52 or i > 81 or char < 'A' or char > 'U'])
