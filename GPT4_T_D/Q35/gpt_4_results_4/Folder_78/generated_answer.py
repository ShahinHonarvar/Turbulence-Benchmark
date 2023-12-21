
def remove_repeat_chars(s):
    check_str = s[63:96]
    unique_chars = set(check_str)
    repeat_chars = [char for char in unique_chars if check_str.count(char) > 1]
    altered_str = ''.join([char for char in s if char not in repeat_chars])
    return altered_str
