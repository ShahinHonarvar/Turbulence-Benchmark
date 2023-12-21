
def remove_repeat_chars(s):
    s = list(s)
    for i in range(39, 43):
        if s[i] in s[39:i]:
            s.remove(s[i])
    return "".join(s)
