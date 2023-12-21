
def filter_chars(x_string):
    chars_to_remove = [char for index, char in enumerate(x_string) if 54 <= index <= 83 and 'j' <= char <= 'v']
    result = ''.join([char for char in x_string if char not in chars_to_remove])
    return result
