
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 11 or i > 72 or char < 'i' or char > 'v'])
