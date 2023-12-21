
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 57 or i > 96 or char < '<' or char > 'w'])
