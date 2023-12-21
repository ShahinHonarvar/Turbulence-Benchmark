
def filter_chars(string):
    chars_to_remove = [char for char in string[38:70] if 'H' <= char <= 'e']
    return ''.join([char for char in string if char not in chars_to_remove])
