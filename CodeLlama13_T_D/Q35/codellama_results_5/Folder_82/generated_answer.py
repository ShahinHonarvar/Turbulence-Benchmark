
def remove_repeat_chars(s):
    seen = {}
    new_s = ""
    for i, c in enumerate(s[30:200]):
        if c not in seen or seen[c] > 1:
            continue
        seen[c] = seen.get(c, 0) + 1
        new_s += c
    return new_s
