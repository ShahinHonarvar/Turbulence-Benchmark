def if_contains_anagrams(test_list):
    res = False
    for i in range(0, len(test_list)):
        for j in range(0, len(test_list)):
            if (test_list[i] == test_list[j] and test_list[i] not in ['', ' ']):
                res = True
                break
    return res
