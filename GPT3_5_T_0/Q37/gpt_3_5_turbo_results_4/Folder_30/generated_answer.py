
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 41 or i > 64 or char < 'K' or char > ']'])
