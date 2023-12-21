
def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[8:10] if 'R' <= char <= 't']
    return ''.join([char for char in input_string if char not in chars_to_remove])
