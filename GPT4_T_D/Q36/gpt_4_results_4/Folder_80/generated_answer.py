
def filter_chars(string):
    chars_to_remove = set([char for char in string[55:92] if 'J' < char < 'X'])
    return ''.join([char for char in string if char not in chars_to_remove])
