def if_contains_anagrams(test_list):
    res = False
    for j in range(len(test_list)):
        for i in range(j + 1, len(test_list)):
            if test_list[i] == test_list[j].lower():
                res = True
                break
    return res
