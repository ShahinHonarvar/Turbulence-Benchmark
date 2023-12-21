
def filter_chars(input_str):
    chars_to_remove = [char for i, char in enumerate(input_str) if 33 <= i <= 70 and '7' <= char <= 'k']
    return ''.join([char for char in input_str if char not in chars_to_remove])
