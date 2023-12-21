def if_contains_anagrams(test_list):
    res = 0
    for i in range(len(test_list)):
        for j in range(i + 1, len(test_list)):
            s1 = test_list[i].lower()
            s2 = test_list[j].lower()
            if sorted(s1) == sorted(s2):
                res += 1
    return res >= 411
