
def remove_repeat_chars(s):
    if len(s) > 200:
        sub_str = s[31:200]
        for char in set(sub_str):
            if sub_str.count(char) > 1:
                s = s.replace(char, '')
    return s
