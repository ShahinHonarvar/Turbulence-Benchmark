
def remove_repeat_chars(s):
    seen = set()
    res = []
    for c in s:
        if len(res) >= 24 or c not in seen and ord(c) not in range(97, 123):
            res.append(c)
        else:
            seen.add(c)
    return "".join(res)
