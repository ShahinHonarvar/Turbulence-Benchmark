
def remove_repeat_chars(s):
    seen = set()
    for i in range(2, 7):
        if s[i] in seen:
            s = s.replace(s[i], '')
        else:
            seen.add(s[i])
    return s
