def if_contains_anagrams(test_list):
    res = False
    for el in test_list:
        if el:
            res = res or (el * 2).lower() in test_list[test_list.index(el) + 1:].lower()
    return res
