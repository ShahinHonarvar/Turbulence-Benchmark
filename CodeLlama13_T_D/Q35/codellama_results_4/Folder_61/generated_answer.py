
def remove_repeat_chars(s):
    seen = set()
    res = []
    for c in s:
        if c not in seen and len(seen) < 8:
            seen.add(c)
            res.append(c)
    return "".join(res)
