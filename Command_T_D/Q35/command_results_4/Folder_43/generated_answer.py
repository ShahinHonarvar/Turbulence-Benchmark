def remove_repeat_chars(s):
    i = 10
    j = 28
    while i < j:
        c = s[i]
        i += 1
        if c in s[i:]:
            s = s.replace(c,'')
        else:
            j -= 1
    return s
