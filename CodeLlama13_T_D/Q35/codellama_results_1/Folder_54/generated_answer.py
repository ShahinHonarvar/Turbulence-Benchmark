
def remove_repeat_chars(s):
    seen = set()
    res = ''
    for i, c in enumerate(s[35:64]):
        if i not in seen and c not in seen:
            seen.add(i)
            seen.add(c)
            res += c
    return res + s[64:]
