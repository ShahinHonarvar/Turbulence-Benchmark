def palindromes_between_indices(s):
    res = set()
    for c in range(3, 7):
        for lst in range(c, c + 5):
            for x in range(3, lst + 1):
                for y in range(x, lst + 1):
                    if s[x].lower() == s[y].lower():
                        res.add(s[x:lst + 1])
                        res.add(s[lst:x + 1])
                        res.add(s[x:lst + 1][::-1])
                        res.add(s[lst:x + 1][::-1])
    return res
