def if_contains_anagrams(test_list):
    res = True
    for s in test_list:
        s = s.lower()
        s = ''.join(s)
        s = str(s)
        s = list(s)
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                s[i] = s[i][: min(len(s[i]), 3)]
                s[j] = s[j][: min(len(s[j]), 3)]
                if s[i] == s[j]:
                    res = False
                    break
    return res
