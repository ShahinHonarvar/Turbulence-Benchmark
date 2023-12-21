def if_contains_anagrams(test_list):
    res = False
    for s in test_list:
        res |= any(a == s.lower() for a in range(1, len(s) + 1))
    return res
