
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 21 or i > 43 or char < '+' or char > '8'])
