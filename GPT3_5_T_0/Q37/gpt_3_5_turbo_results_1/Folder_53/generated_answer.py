
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 83 or i > 99 or char < '*' or char > 'j'])
