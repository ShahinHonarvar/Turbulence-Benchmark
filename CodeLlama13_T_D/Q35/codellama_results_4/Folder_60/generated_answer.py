
def remove_repeat_chars(s):
    for i in range(38, 52):
        if s[i] in s and s[i] != s[i-1]:
            s = s.replace(s[i], "")
    return s
