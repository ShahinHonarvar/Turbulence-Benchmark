
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[307:807] if s[307:807].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
