
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[82:86] if s[82:86].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
