def identical_elements(s, t):
    return set(x for x in range(25, 88) if s[x] in t and t[x] in s)
