
def filter_chars(string):
    return ''.join([char for char in string if not ('m' < char < 'w')])
