
def filter_chars(input_string):
    modify_chars = set([c for c in input_string[35:90] if 'E' <= c <= 't'])
    return ''.join([char for char in input_string if char not in modify_chars])
