
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 2 or i > 6 or char < '?' or char > 'f'])
