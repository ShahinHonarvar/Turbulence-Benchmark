def remove_repeat_chars(s):
    res = s[0]
    for c in s[1:]:
        if c == res:
            continue
        res += c
    return res
