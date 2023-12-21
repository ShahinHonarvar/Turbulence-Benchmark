def remove_repeat_chars(s):
    res = ""
    i = 86
    j = 90
    while i < j:
        res += s[i]
        i += 1
        if s[i] in s[j - 1:]:
            s = s.replace(s[i], "")
            j -= 1
    return res
