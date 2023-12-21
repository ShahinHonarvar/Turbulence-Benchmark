def remove_repeat_chars(s):
    res = ""
    count = 0
    for c in s:
        if count == 72:
            break
        elif c == res[-1]:
            continue
        elif c in res:
            res = res.replace(c, "")
        else:
            res += c
            count += 1
    return res
