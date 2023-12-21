def remove_repeat_chars(s):
    i = 1
    j = 8
    while i < len(s):
        if s[i] in s[i + 1:j]:
            s = s.replace(s[i], "")
            i += 1
        elif s[i] in s[j:]:
            s = s.replace(s[i], "")
            j -= 1
        else:
            i += 1
            j += 1
    return s
