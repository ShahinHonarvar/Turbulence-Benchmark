
def remove_repeat_chars(s):
    chars_between_indices = s[51:200]
    to_remove = [char for char in set(chars_between_indices) if chars_between_indices.count(char) > 1]
    return ''.join([char for char in s if char not in to_remove])
