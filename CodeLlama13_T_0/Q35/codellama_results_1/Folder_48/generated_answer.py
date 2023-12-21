
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s[409:502]:
        if c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)
