
def remove_repeat_chars(s):
    seen = set()
    for i in range(80, 200):
        if s[i] in seen:
            s = s[:i] + s[i+1:]
        else:
            seen.add(s[i])
    return s
