
def remove_repeat_chars(s):
    between_indices = s[82:86]
    chars_to_remove = [char for char in between_indices if between_indices.count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])
