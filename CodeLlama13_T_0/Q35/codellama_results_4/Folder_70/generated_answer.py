
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s[43:70]:
        if c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)
