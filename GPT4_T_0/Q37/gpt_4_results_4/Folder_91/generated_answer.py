
def filter_chars(s):
    chars_to_remove = [char for char in s[7:9] if 'B' <= char <= 'H']
    return ''.join([char for char in s if char not in chars_to_remove])
