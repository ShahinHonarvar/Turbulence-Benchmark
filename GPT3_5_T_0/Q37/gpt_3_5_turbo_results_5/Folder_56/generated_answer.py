
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 71 or i > 94 or char < 'K' or char > 'a'])
