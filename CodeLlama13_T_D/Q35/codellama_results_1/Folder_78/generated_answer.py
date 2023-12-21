
def remove_repeat_chars(s):
    seen = {}
    for i in range(62, 96):
        if s[i] in seen:
            s = s[:i] + s[i+1:]
        else:
            seen[s[i]] = True
    return s
