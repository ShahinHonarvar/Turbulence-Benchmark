
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 259 or i > 502 or char < ',' or char > '3'])
