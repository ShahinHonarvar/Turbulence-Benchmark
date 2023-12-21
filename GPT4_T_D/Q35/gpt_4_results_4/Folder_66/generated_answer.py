
def remove_repeat_chars(s):
    sub_str = s[12:76]
    unique_chars = set(sub_str)
    for char in unique_chars:
        if sub_str.count(char) > 1:
            s = s.replace(char, '')
    return s
