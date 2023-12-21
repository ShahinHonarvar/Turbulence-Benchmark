def remove_repeat_chars(s):
    res = ""
    for i in range(len(s) - 1):
        res += s[i]
        if s[i] in s[i + 1:]:
            res += s[i + 1:]
        i += 1
    return res
