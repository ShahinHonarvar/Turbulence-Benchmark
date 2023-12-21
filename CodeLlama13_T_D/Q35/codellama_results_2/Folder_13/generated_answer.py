
def remove_repeat_chars(s):
    s = list(s)
    for i in range(46, 91):
        if s[i] in s[46:i]:
            s.remove(s[i])
    return ''.join(s)
