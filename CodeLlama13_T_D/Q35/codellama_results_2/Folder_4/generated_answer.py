
def remove_repeat_chars(s):
    seen = set()
    res = []
    for c in s[49:75]:
        if c not in seen:
            res.append(c)
            seen.add(c)
    return "".join(res)
