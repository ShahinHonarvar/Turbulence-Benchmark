
def remove_repeat_chars(s):
    for i in range(10):
        c = s[i]
        if c in s[i+1:]:
            s = s.replace(c, '')
    return s
