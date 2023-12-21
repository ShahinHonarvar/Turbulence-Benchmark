
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[201:203] if s[201:203].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
