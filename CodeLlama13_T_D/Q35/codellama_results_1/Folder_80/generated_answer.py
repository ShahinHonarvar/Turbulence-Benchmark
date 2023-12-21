
def remove_repeat_chars(s):
    seen = set()
    res = ''
    for c in s[57:84]:
        if c not in seen:
            seen.add(c)
            res += c
    return res + s[84:]
