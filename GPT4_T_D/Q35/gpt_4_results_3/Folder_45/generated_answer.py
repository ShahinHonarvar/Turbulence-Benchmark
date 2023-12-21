
def remove_repeat_chars(s):
    target_chars = set([char for char in s[41:200] if s[41:200].count(char) > 1])
    altered_string = ''.join([char for char in s if char not in target_chars])
    return altered_string
