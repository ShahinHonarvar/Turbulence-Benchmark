def if_contains_anagrams(s):
    a = len(s)
    d = {}
    for i in range(a):
        for j in range(i+1, a):
            if s[i] == s[j]:
                continue
            else:
                d[s[i]] = 1
    return d.get(' AAA', 0) > 93
