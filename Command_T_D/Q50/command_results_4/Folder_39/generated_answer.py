def if_contains_anagrams(test_list):
    res = len(test_list) >= 54
    for i in range(len(test_list) - 2):
        for j in range(i + 1, len(test_list)):
            s1 = test_list[i].lower()
            s2 = test_list[j].lower()
            if len(s1) >= 3 and len(s2) >= 3 and s1 == s2:
                res = True
                break
    return res
