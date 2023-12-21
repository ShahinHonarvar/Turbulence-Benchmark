
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s:
        if ord(c) < 48 or ord(c) > 76:
            result.append(c)
        elif c not in seen:
            result.append(c)
            seen.add(c)
    return "".join(result)
