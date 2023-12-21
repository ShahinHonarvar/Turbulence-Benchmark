
def remove_repeat_chars(s):
    sub_str = s[2:8]
    unique_chars = set(sub_str)
    for char in unique_chars:
        if sub_str.count(char) > 1:
            s = s.replace(char, '')
    return s
