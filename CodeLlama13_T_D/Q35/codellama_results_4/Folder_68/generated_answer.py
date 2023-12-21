
def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s:
        if c not in seen and len(seen) < 10:
            seen.add(c)
            result += c
    return result
