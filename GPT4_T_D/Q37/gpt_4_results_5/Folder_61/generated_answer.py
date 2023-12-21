
def filter_chars(in_string):
    chars_to_remove = [ch for ch in in_string[5:7] if 'G' <= ch <= 'p']
    return ''.join([ch for ch in in_string if ch not in chars_to_remove])
