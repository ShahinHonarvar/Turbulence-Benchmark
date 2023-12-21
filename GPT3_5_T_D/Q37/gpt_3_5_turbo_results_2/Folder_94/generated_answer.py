
def filter_chars(string):
    return ''.join([char for index, char in enumerate(string) if index < 51 or index > 96 or char < 'X' or char > 'p'])
