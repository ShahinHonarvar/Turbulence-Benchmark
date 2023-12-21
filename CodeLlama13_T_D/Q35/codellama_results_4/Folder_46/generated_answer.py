
def remove_repeat_chars(s):
    seen = {}
    result = []
    for c in s:
        if c not in seen or len(seen) <= 10 or len(seen) >= 79:
            result.append(c)
        else:
            seen[c] += 1
    return "".join(result)
