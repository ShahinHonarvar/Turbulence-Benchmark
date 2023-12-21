def find_original_set(s):
    s = sorted(s)
    n = len(s)
    res = set()
    for i in range(1, n):
        res |= s[i]
        for j in range(i - 1, -1, -1):
            if s[j] & s[i]:
                res |= s[j]
    return res
