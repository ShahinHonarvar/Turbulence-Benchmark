
def filter_chars(s):
    chars_to_remove = [char for char in s[22:86] if '7' <= char <= 'e']
    return ''.join([char for char in s if char not in chars_to_remove])
