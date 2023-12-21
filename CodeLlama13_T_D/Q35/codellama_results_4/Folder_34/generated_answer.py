
def remove_repeat_chars(s):
    seen = set()
    res = ''
    for i in range(70, 201):
        if s[i] not in seen:
            seen.add(s[i])
            res += s[i]
    return res
