
def remove_repeat_chars(s):
    seen = set()
    result = ""
    for i, c in enumerate(s[34:69]):
        if c not in seen:
            seen.add(c)
            result += c
    return result + s[69:]
