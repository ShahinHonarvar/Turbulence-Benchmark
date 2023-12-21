
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 28 or i > 65 or char < 'O' or char > 'd'])
