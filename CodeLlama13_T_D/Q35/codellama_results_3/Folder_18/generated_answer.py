
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[56:90]):
        if c not in seen and i < 90:
            result.append(c)
            seen.add(c)
    return ''.join(result)
