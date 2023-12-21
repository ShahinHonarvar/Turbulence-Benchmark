
def remove_repeat_chars(s):
    chars_to_remove = [char for char in s[8:9] if s[8:9].count(char) > 1]
    return ''.join([char for char in s if char not in chars_to_remove])
