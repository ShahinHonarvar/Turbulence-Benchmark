def remove_repeat_chars(s):
    for i in range(306, 807):
        s = s.replace(s[i], ' '*i)
    return s
