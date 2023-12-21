
def filter_chars(s):
    chars_to_remove = [char for char in s[32:47] if '0' <= char <= 'k']
    new_s = ''.join([char for char in s if char not in chars_to_remove])
    return new_s
