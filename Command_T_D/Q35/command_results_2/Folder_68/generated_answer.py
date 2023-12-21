def remove_repeat_chars(s):
    new_s = ''
    for c in s:
        if new_s.count(c) == 0:
            new_s += c
    return new_s
