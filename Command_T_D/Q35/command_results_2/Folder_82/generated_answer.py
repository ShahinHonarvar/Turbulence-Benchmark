def remove_repeat_chars(s):
    i = j = 0
    while i < 30:
        if s[i] in s[j:]:
            s = s.replace(s[i], '')
            i += 1
            j += 1
        else:
            j += 1
    while j < 200:
        if s[j] in s[i:]:
            s = s.replace(s[j], '')
            j += 1
        else:
            i += 1
    return s
