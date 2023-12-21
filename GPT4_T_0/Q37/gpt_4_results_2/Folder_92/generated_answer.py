
def filter_chars(s):
    chars_to_remove = [char for char in s[4:5] if '7' <= char <= 'o']
    return ''.join([char for char in s if char not in chars_to_remove])
