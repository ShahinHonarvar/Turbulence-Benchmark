
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s[38:52]:
        if c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)
