
def remove_repeat_chars(s):
    n = len(s)
    sub_str = s[2:4]
    for char in set(sub_str):
        if sub_str.count(char) > 1:
            s = s[:2] + s[2:].replace(char, '')
    return s
