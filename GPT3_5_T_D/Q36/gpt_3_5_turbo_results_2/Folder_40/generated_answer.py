
def filter_chars(string):
    return ''.join([char for char in string if char <= '-' or char >= 'L'])
