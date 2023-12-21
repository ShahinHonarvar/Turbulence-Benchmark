
def remove_repeat_chars(s):
    seen = {}
    result = []
    for c in s:
        if c not in seen or len(seen) < 7:
            result.append(c)
            seen[c] = True
    return "".join(result)
