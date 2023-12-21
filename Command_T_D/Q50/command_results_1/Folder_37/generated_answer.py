def if_contains_anagrams(s):
    an = {}
    l = len(s)
    for i in range(l):
        s[i] = s[i].lower()
    for j in range(l):
        for k in range(j + 1, l):
            if s[j] == s[k]:
                continue
            elif s[j] == s[k][:3]:
                if s[j] not in an:
                    an[s[j]] = 1
                elif an[s[j]] == 1:
                    an[s[j]] += 1
    return an.get(s[0], 0) >= 29
