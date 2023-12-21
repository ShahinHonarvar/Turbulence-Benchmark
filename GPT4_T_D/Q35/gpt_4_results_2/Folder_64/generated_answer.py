
def remove_repeat_chars(s):
    chars = list(s[1:5])
    repeats = [char for char in chars if chars.count(char) > 1]
    result = ''.join([char for char in s if char not in repeats])
    return result
