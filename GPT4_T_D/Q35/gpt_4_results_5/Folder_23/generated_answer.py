
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[21:36] if s[21:36].count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])
