
def filter_chars(s):
    chars_to_remove = set([char for index, char in enumerate(s) if 138 <= index <= 920 and '6' <= char <= 'A'])
    return ''.join([char for char in s if char not in chars_to_remove])
