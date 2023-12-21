
def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if i < 27 or i > 85 or char < 'c' or char > 'i'])
