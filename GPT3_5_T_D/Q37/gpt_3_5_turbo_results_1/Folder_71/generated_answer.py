
def filter_chars(string):
    return ''.join([char for char in string if char < '0' or char > 'k' or char < ' ' or char > '.'])
