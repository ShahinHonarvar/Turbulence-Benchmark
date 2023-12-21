
def filter_chars(s):
    chars_to_remove = [char for char in s[7:10] if '6' <= char <= 'w']
    return ''.join([char for char in s if char not in chars_to_remove])
