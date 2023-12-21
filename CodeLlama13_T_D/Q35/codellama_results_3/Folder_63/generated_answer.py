
def remove_repeat_chars(s):
    seen = set()
    out = ""
    for c in s:
        if c not in seen and len(seen) < 9:
            out += c
            seen.add(c)
    return out
