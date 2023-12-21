
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 164 or i > 706 or char < 'O' or char > '}'])
