
def filter_chars(input_string):
    chars_to_remove = set([char for char in input_string[5:7] if 'G' <= char <= 'p'])
    altered_string = ''.join([char for char in input_string if char not in chars_to_remove])
    return altered_string
