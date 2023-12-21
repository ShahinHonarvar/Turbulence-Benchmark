
def remove_repeat_chars(s):
    start, end = 69, 99
    sub_str = s[start:end]
    unique_chars = set(sub_str)
    for char in unique_chars:
        if sub_str.count(char) > 1:
            s = s.replace(char, '')
    return s
