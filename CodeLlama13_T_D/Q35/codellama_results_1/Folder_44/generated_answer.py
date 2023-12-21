
def remove_repeat_chars(s):
    seen = set()
    out = []
    for c in s[36:52]:
        if c not in seen:
            seen.add(c)
            out.append(c)
    return "".join(out)
