def remove_repeat_chars(s):
    for i in range(45, 48):
        if s[i] in s[i - 1:]:
            s = s.replace(s[i], '').replace(s[i], '')
    return s
