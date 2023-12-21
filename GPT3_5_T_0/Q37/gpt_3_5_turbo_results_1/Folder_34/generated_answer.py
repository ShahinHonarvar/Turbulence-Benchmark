
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 54 or i > 62 or char < ')' or char > '9'])
