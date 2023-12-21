
def filter_chars(s):
    start_index = 83
    end_index = 99
    chars_to_remove = set([char for char in s[start_index:end_index + 1] if '*' <= char <= 'j'])
    return ''.join([char for char in s if char not in chars_to_remove])
