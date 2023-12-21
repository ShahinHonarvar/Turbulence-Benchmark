
def remove_repeat_chars(s):
    seen = set()
    res = []
    for i in range(90, 200):
        if s[i] not in seen:
            seen.add(s[i])
            res.append(s[i])
    return "".join(res)
