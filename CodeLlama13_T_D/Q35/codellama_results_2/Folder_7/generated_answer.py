
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s:
        if c not in seen and len(result) < 926:
            result.append(c)
            seen.add(c)
    return "".join(result)
