
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[23:24] if s[23:24].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
