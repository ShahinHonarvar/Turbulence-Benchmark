
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[20:32] if s[20:32].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
