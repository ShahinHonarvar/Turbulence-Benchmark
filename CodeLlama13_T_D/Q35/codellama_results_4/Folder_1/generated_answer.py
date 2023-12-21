
def remove_repeat_chars(s):
    seen = set()
    result = []
    for c in s[17:88]:
        if c not in seen:
            result.append(c)
            seen.add(c)
    return ''.join(result)
