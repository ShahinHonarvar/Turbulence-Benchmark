
def filter_chars(input_string):
    target_chars = set([c for c in input_string[332:713] if 'M' < c < '_'])
    return ''.join([c for c in input_string if c not in target_chars])
