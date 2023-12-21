
def filter_chars(input_string):
    chars_to_remove = [char for char in input_string[35:52] if 'H' <= char <= 's']
    char_set = set(chars_to_remove)
    return ''.join([char for char in input_string if char not in char_set])
