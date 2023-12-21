
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 379 or i > 898 or char < 'M' or char > 'v'])
