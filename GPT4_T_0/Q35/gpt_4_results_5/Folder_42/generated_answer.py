
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[19:60] if s[19:60].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
