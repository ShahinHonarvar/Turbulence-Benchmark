
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 36 or i > 79 or char < '2' or char > 's'])
