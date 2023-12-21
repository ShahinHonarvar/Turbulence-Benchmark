def remove_repeat_chars(s):
    for i in range(32, 45):
        s = s.replace(chr(i), "")
    return s
