
def remove_repeat_chars(s):
    for i in range(70, 201):
        c = s[i]
        if s[i-1:i+1].count(c) > 1:
            s = s.replace(c, '')
    return s
