
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for i, c in enumerate(s[476:709]):
        if c not in seen and i < 709:
            seen.add(c)
            result += c
    return result + s[709:]
