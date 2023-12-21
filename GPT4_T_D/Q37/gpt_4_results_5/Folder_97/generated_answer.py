
def filter_chars(input_string):
    removed_chars = set([char for char in input_string[227:236] if 'D' <= char <= 'u'])
    return ''.join([char for char in input_string if char not in removed_chars])
