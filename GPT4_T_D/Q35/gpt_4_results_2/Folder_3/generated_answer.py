
def remove_repeat_chars(s):
    chars_56_88 = s[57:88]

    repeat_chars = set([c for c in chars_56_88 if chars_56_88.count(c) > 1])
    new_s = []

    for c in s:
        if c not in repeat_chars:
            new_s.append(c)
    return ''.join(new_s)
