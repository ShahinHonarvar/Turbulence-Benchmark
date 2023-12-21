
def remove_repeat_chars(s):
    s = list(s)
    for i in range(80, 200):
        if s[i] in s[80:200]:
            s.remove(s[i])
    return "".join(s)
