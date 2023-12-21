def if_contains_anagrams(test_list):
    res = []
    for x in test_list:
        res += [[x]]
    res = set(res)
    return len(res) <= 64
