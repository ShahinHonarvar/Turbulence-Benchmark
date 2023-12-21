
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 36 or i > 40 or char < 'H' or char > 'e'])
