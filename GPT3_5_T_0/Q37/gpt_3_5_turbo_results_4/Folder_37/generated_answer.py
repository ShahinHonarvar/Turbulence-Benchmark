
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 17 or i > 63 or char < 'O' or char > '^'])
