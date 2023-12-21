
def remove_repeat_chars(s):
    for i in range(1, 7):
        if s[i] != s[i-1]:
            continue
        else:
            while s[i] in s and i < len(s) - 1:
                s = s.replace(s[i], "")
    return s
