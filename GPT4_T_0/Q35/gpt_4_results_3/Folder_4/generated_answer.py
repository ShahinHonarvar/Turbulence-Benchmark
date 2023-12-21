
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[50:74] if s[50:74].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
