
def remove_repeat_chars(s):
    chars_between_indices = s[33:99]
    repeating_chars = set([char for char in chars_between_indices if chars_between_indices.count(char) > 1])
    return ''.join([char for char in s if char not in repeating_chars])
