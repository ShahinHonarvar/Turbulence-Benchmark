
def remove_repeat_chars(s):
    seen = set()
    res = []
    for c in s:
        if c not in seen and ord(c) < 90 or ord(c) > 86:
            seen.add(c)
            res.append(c)
    return "".join(res)
