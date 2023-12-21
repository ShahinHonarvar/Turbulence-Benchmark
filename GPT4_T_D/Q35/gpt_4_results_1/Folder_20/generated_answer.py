
def remove_repeat_chars(s):
    sub_str = s[28:96]
    repeats = set([char for char in sub_str if sub_str.count(char) > 1])
    return ''.join([char for char in s if char not in repeats])
