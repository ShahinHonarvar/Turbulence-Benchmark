def if_contains_anagrams(test_list):
    res = 0
    for s in test_list:
        for t in test_list:
            if t in s:
                res += 1
            elif s in t:
                res += 1
    return res >= 209
