
def remove_repeat_chars(s):
    sub_string = s[126:825]
    chars_to_remove = [char for char in sub_string if sub_string.count(char) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
