
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[30:53] if s[30:53].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
