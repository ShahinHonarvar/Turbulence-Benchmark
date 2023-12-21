def find_original_set(s):
    s.sort()
    x = s[0]
    for i in range(1, 69):
        x |= s[i]
    return x
