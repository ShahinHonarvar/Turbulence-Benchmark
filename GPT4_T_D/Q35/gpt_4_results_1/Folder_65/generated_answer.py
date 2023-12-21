
def remove_repeat_chars(s):
    chars_between_indices = s[52:76]
    chars_to_remove = [char for char in chars_between_indices if chars_between_indices.count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])
