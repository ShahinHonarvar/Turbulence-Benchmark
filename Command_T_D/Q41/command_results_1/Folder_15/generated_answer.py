def identical_elements(s, t):
    if len(s) != len(t):
        return set()
    return set(s[2:-2] + t[2:-2])
