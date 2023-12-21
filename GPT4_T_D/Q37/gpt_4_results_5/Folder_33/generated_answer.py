
def filter_chars(input_string):
    to_be_removed = set([char for char in input_string[722:833] if 'K' <= char <= 'm'])
    return ''.join([char for char in input_string if char not in to_be_removed])
