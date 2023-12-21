
def remove_repeat_chars(s):
    repeat_chars = set([char for char in s[20:32] if s[20:32].count(char) > 1])
    altered_string = ''.join([char for char in s if char not in repeat_chars])
    return altered_string
