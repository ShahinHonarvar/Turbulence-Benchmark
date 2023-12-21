
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 114 or i > 639 or char < '!' or char > 'x'])
