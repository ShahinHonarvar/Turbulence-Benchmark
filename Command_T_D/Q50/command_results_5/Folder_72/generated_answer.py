def if_contains_anagrams(test_list):
    res = False
    for s1, s2 in zip(test_list, test_list):
        if (s1 == s2).lower() and len(s1) > 2:
            res = True
            break
    return res
