
def remove_repeat_chars(s):
    repeat_chars = [char for char in s[45:67] if s[45:67].count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
