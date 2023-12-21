
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 4 or char < '7' or char > 'o'])
