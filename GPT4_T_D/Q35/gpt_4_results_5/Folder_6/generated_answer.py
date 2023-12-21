
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[21:93] if s[21:93].count(char) > 1])
    result = ''.join([char for char in s if char not in repeat_chars])
    return result
