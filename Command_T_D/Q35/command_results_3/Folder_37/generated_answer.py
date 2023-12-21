def remove_repeat_chars(s):
    i = 2
    j = 7
    while i < j:
        if s[i] in s[i + 1:j]:
            s = s.replace(s[i], "")
        i += 1
        j -= 1
    return s
