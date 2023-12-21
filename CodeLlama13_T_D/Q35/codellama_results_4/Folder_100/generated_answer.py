
def remove_repeat_chars(s):
    for i in range(44, 78):
        if s[i] in s[:i]:
            s = s.replace(s[i], "")
    return s
