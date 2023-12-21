
def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for i, c in enumerate(s[25:80]):
        if c not in seen:
            seen.add(c)
            new_s += c
    return new_s + s[:25] + s[80:]
