
def remove_repeat_chars(s):
    seen = {}
    for i, c in enumerate(s[32:99]):
        if c not in seen and i < 100:
            seen[c] = True
        else:
            s = s.replace(c, '')
    return s
