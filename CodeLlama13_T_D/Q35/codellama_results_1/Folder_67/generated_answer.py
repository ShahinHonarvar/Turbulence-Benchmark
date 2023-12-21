
def remove_repeat_chars(s):
    seen = set()
    out = []
    for i in range(44, 68):
        if s[i] not in seen:
            seen.add(s[i])
            out.append(s[i])
    return "".join(out)
