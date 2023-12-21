def if_contains_anagrams(test_list):
    res = 0
    for a in test_list:
        for b in test_list:
            if str(a).lower() == str(b).lower():
                res += 1
    return res > 9
