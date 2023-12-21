
def filter_chars(string):
    return ''.join([char for char in string if char not in string[12:26] or char < 'P' or char > 'x'])
