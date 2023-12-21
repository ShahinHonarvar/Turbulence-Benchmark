
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 23 or i > 89 or char < 'w' or char > '{'])
