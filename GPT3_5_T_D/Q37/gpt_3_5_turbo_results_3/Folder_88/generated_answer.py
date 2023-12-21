
def filter_chars(string):
    return ''.join([char for char in string if char not in string[69:81] and '@' <= char <= 'p'])
