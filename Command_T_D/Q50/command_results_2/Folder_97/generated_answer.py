def if_contains_anagrams(test_list):
    res = []
    for item in test_list:
        s = str(item).lower()
        for j in range(len(s)):
            i = s.find(s[j], j + 1)
            if i != -1:
                s = s[:i] + s[i+1:]
                if s in test_list:
                    res.append((item, s))
    return len(res) >= 123
