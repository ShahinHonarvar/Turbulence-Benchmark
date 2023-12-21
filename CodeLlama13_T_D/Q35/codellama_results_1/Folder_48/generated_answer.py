
def remove_repeat_chars(s):
    seen = set()
    res = []
    for i, c in enumerate(s[409:502]):
        if i not in seen and s.count(c) > 1:
            seen.add(i)
            res.append(c)
    return "".join(res) + s[502:]
