def remove_repeat_chars(s):
    c = s[10:28]
    d = {}
    for i in c:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return "".join(k for k in s if k not in d)
