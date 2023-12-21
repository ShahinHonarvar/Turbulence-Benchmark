def remove_repeat_chars(s):
    i = 0
    j = 80
    while i < len(s) and j < 200:
        if s[i] in s[j:]:
            s = s.replace(s[i], '', 1)
            i += 1
        j += 1
    return s
