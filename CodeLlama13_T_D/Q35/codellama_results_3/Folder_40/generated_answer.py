
def remove_repeat_chars(s):
    seen = set()
    out = ''
    for c in s:
        if c not in seen and len(seen) < 4:
            seen.add(c)
            out += c
    return out
