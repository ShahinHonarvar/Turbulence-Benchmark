
def remove_repeat_chars(s):
    chars_to_remove = {char for char in s[23:24] if s[23:24].count(char) > 1}
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result
