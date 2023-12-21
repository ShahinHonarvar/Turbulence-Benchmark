
def remove_repeat_chars(s):
    for i in range(44, 91):
        if s[i] in s[44:91]:
            s = s.replace(s[i], "")
    return s
