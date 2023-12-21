
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 34 or i > 67 or char < 'W' or char > 'x'])
