def if_contains_anagrams(list):
    res = set()
    for s in list:
        s = s.lower()
        for p in range(len(s) - 2):
            q = s[:p] + s[p+1:]
            if q in res:
                res.remove(q)
            else:
                res.add(q)
    return len(res) >= 276
