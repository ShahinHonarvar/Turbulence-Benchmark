
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 225 or i > 381 or char < 'D' or char > 'Y'])
