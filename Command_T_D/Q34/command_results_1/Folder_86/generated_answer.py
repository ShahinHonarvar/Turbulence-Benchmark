def find_original_set(s):
    d = {}
    for i in range(len(s)):
        d[s[i]] = 1
    return set(k for k in range(len(d)) if d[k])
