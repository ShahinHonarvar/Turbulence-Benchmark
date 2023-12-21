
def filter_chars(input_string):
    char_to_remove = set([char for char in input_string[20:63] if 'i' <= char <= 'k'])
    return ''.join([char for char in input_string if char not in char_to_remove])
