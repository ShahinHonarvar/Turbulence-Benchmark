
def remove_repeat_chars(s):
    substring = s[71:200]
    repeats = [char for char in substring if substring.count(char) > 1]
    result = ''.join([char for char in s if char not in repeats])
    return result
