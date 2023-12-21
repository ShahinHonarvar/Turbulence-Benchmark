
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 20 or i > 79 or char < '!' or char > 'T'])
