
def remove_repeat_chars(s):
    s_to_check = s[61:200]
    repeat_chars = [char for char in s_to_check if s_to_check.count(char) > 1]
    result = ''.join([char for char in s if char not in repeat_chars])
    return result
