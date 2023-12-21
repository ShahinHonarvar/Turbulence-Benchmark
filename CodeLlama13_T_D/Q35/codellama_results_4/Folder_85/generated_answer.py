
def remove_repeat_chars(s):
    seen = {}
    result = []
    for c in s:
        if c not in seen or seen[c] > 1:
            result.append(c)
        else:
            seen[c] = seen.get(c, 0) + 1
    return "".join(result)
