
def remove_repeat_chars(s):
    substring = s[63:96]
    repeat_chars = [char for char in substring if substring.count(char) > 1]
    return ''.join([char for char in s if char not in repeat_chars])
