def remove_repeat_chars(s):
    res = ""
    for c in s:
        res += c
        if c in s[90:200]:
            res += s[90:200].replace(c, "")
    return res
