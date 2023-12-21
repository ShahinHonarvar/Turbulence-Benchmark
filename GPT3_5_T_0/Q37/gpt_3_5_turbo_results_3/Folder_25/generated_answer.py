
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 31 or i > 38 or char < ';' or char > 'g'])
