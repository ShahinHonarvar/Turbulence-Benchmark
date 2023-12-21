
def remove_repeat_chars(s):
    seen = set()
    res = ''
    for c in s:
        if c[34:69] and c not in seen:
            res += c
            seen.add(c)
        elif c[34:69] and c in seen:
            pass
        else:
            res += c
    return res
