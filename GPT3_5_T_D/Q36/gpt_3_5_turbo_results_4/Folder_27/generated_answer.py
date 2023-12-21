
def filter_chars(string):
    return ''.join([char for char in string if not ('6' < char < '_')])
