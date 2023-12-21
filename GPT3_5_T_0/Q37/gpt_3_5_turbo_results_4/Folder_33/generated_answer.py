
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 722 or i > 832 or char < 'K' or char > 'm'])
