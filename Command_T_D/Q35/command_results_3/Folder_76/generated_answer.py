def remove_repeat_chars(s):
    for i in range(len(s) - 1, 330 - 1, -1):
        if s[i] in s[i + 1:]:
            s = s.replace(s[i], "")
    for i in range(len(s) - 1, 543 - 1, -1):
        if s[i] in s[i + 1:]:
            s = s.replace(s[i], "")
    return s
