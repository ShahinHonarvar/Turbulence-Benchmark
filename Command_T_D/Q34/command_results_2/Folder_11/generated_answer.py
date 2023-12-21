def find_original_set(s):
    s.sort()
    res = set()
    for i in range(len(s)):
        res |= s[i]
    return res
