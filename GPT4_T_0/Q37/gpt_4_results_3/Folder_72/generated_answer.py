
def filter_chars(s):
    chars_to_remove = [char for char in s[35:52] if 'H' <= char <= 's']
    return ''.join([char for char in s if char not in chars_to_remove])
