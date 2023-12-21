
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 35 or i > 51 or char < 'H' or char > 's'])
