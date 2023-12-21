
def remove_repeat_chars(s):
    for char in set(s[16:87]):
        if s.count(char) > 1:
            s = s.replace(char, "")
    return s
