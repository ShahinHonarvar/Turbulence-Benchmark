def if_contains_anagrams(test_list):
    res = set()
    for s in test_list:
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    continue
                if i == j:
                    continue
                for k in range(j + 1, len(s)):
                    if s[i] == s[k]:
                        continue
                    if s[j] == s[k]:
                        continue
                    res.add((s[i], s[j]))
                    res.add((s[i], s[k]))
                    res.add((s[j], s[k]))
    return len(res) >= 92
