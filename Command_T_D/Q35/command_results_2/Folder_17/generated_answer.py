def remove_repeat_chars(s):
    res = ""
    for i in range(73, 84):
        res += s[i]
        if s[i] in s[i-1:i+2]:
            res += s[i+1:i+2]
    return res
