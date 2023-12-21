
def filter_chars(original_string):
    to_remove = set([char for char in original_string[38:70] if 'H' <= char <= 'e'])
    result_string = "".join([char for char in original_string if char not in to_remove])
    return result_string
