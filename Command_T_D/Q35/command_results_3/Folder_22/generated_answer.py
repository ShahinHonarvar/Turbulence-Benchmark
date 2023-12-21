def remove_repeat_chars(s):
    res = ""
    count = 1
    for i in range(50, 201):
        if s[i] in res:
            continue
        elif s[i] in s[50:i]:
            count += 1
        elif count > 2:
            res += s[i]
            count = 1
        else:
            res += s[i]
            count += 1
    return res
