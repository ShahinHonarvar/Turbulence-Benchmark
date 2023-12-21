
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 12 or i > 77 or char < ':' or char > 'L'])
