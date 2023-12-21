
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[34:78] if s[34:78].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
