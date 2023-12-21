def find_original_set(s):
    res = set(s)
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                if s[i] & s[j] & s[k]:
                    res.discard(s[i])
                    res.discard(s[j])
                    res.discard(s[k])
    return res
