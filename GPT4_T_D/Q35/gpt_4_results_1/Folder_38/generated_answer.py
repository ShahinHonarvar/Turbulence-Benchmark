
def remove_repeat_chars(s):
    middle_range = s[37:85]
    remove_char = {char for char in middle_range if middle_range.count(char) > 1}
    return ''.join([char for char in s if char not in remove_char])
