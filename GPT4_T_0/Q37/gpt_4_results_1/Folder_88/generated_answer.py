
def filter_chars(s):
    chars_to_remove = [char for i, char in enumerate(s) if 69 <= i <= 80 and '@' <= char <= 'p']
    return ''.join([char for char in s if char not in chars_to_remove])
