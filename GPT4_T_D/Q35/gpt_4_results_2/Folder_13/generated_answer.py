
def remove_repeat_chars(s):
    sub_s = s[47:91]
    for char in set(sub_s):
        if sub_s.count(char) > 1:
            s = s.replace(char, "")
    return s
