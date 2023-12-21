
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 1 or i > 5 or char < '$' or char > ';'])
