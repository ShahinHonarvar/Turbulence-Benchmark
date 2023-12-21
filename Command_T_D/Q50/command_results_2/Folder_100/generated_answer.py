def if_contains_anagrams(test_list):
    res = 0
    for a in test_list:
        for b in test_list:
            if a.lower() == b.lower():
                res += 1
    return res >= 95
