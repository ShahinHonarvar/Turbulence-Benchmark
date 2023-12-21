
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 124 or i > 854 or char < '9' or char > 's'])
