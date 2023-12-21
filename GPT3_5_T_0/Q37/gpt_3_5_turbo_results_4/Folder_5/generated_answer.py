
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 24 or i > 82 or char < '5' or char > '<'])
