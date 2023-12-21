
def remove_repeat_chars(s):
    if len(s) > 51:
        s_to_check = s[21:51]
    else:
        return s
    repeat_chars = [char for char in s_to_check if s_to_check.count(char) > 1]
    repeat_chars = list(set(repeat_chars))
    for char in repeat_chars:
        s = s.replace(char, '')
    return s
