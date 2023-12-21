def if_contains_anagrams(test_list):
    res = True
    for idx in range(len(test_list)):
        for jdx in range(idx + 1, len(test_list)):
            if test_list[idx].lower() == test_list[jdx].lower():
                res = False
                break
    return res
