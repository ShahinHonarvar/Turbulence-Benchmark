
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 42 or i > 97 or char < '*' or char > 'b'])
