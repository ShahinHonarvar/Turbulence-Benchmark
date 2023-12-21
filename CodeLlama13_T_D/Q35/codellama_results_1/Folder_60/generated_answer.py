
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[38:52]):
        if c not in seen and i < 52:
            seen.add(c)
            result.append(c)
    return ''.join(result)
