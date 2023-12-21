
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 19 or i > 33 or char < 'S' or char > '{'])
