
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 51 or i > 96 or char < 'X' or char > 'p'])
