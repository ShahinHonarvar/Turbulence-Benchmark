
def remove_repeat_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 20 < i < 200 and s.count(char) > 1}
    return ''.join(char for char in s if char not in chars_to_remove)
