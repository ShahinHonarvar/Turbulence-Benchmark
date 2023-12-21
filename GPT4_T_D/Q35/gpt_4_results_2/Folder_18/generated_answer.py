
def remove_repeat_chars(s):
    sub_str = s[57:90]
    chars_to_remove = [char for char in set(sub_str) if sub_str.count(char) > 1]
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s
