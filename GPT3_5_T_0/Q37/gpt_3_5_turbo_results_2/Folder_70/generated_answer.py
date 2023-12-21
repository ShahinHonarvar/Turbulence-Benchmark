
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 515 or i > 538 or char < '+' or char > '}'])
