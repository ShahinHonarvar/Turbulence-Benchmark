
def remove_repeat_chars(s):
    substring = s[63:96]
    repeats = [char for char in substring if substring.count(char) > 1]
    new_string = ''.join([char for char in s if char not in repeats])
    return new_string
