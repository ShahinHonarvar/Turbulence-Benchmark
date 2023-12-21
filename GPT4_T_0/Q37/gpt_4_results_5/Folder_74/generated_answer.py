
def filter_chars(s):
    chars_to_remove = [char for char in s[19:33] if 'f' <= char <= 'o']
    return ''.join([char for char in s if char not in chars_to_remove])
