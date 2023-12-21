
def remove_repeat_chars(s):
    repeat_chars = []
    for c in set(s[71:200]):
        if s[71:200].count(c) > 1:
            repeat_chars.append(c)
    for c in repeat_chars:
        s = s.replace(c, '')
    return s
