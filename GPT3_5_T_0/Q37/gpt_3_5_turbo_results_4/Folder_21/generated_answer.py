
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 603 or i > 759 or char < 'Q' or char > 'h'])
