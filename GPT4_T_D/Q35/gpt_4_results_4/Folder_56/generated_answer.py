
def remove_repeat_chars(s):
    sub_str = s[8:9]
    for char in sub_str:
        if sub_str.count(char) > 1:
            s = s.replace(char, '')
    return s
