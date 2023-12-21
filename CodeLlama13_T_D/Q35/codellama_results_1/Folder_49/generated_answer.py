
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[90:200]):
        if i < 90 or i >= 200 or c not in seen:
            result.append(c)
            seen.add(c)
    return ''.join(result)
