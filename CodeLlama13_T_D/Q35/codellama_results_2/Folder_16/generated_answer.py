
def remove_repeat_chars(s):
    seen = {}
    for i, c in enumerate(s):
        if 90 <= i < 97 and c in seen:
            s = s.replace(c, "")
        else:
            seen[c] = True
    return s
