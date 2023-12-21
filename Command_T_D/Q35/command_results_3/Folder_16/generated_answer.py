def remove_repeat_chars(s):
    for i in range(90, 97):
        if s[i] in s[90:]:
            s = s.replace(s[i], "")
    return s
