def if_contains_anagrams(s):
    d = {}
    for i in range(len(s) - 2):
        a = s[i]
        for j in range(i + 1, len(s)):
            b = s[j]
            if str(a).lower() == str(b).lower():
                d[a] = d[a] + 1 if d[a] < 60 else False
                d[b] = d[b] + 1 if d[b] < 60 else False
    return d['']
