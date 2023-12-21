
def remove_repeat_chars(s):
    str_to_check = s[14:91]
    unique_chars = set(str_to_check)
    for char in unique_chars:
        if str_to_check.count(char) > 1:
            s = s.replace(char, '')
    return s
