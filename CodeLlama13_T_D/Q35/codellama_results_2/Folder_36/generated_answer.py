
def remove_repeat_chars(s):
    seen = set()
    res = ''
    for c in s[476:709]:
        if c not in seen:
            seen.add(c)
            res += c
    return res + s[709:]
