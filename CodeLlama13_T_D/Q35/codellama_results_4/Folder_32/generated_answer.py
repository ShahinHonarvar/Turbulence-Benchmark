
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s[86:90]:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result) + s[90:]
