def remove_repeat_chars(s):
    i = 86
    j = 89
    while i < j:
        c = s[i]
        i += 1
        if c in s[i:]:
            s = s.replace(c, '')
        else:
            i += 1
    return s
