
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 33 or i > 70 or char < '7' or char > 'k'])
