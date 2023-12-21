
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 46 or i > 85 or char < '-' or char > 'X'])
