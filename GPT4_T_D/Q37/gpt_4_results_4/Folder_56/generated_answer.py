
def filter_chars(string):
    chars_to_remove = [char for char in string[71:95] if 'K' <= char <= 'a']
    return ''.join([char for char in string if char not in chars_to_remove])
