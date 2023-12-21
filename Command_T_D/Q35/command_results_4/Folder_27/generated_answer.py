def remove_repeat_chars(s):
    for i in range(86, 89):
        if s[i] in s[86:]:
            s = s.replace(s[i], '')
    return s
