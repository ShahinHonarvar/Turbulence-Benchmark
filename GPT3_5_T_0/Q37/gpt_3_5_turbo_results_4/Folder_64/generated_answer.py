
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 1 or i > 7 or char < 'L' or char > 'a'])
