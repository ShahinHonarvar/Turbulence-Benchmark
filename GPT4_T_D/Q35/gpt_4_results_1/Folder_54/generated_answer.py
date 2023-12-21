
def remove_repeat_chars(s):
    chars_in_range = s[36:64]
    chars_to_remove = [char for char in chars_in_range if chars_in_range.count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])
