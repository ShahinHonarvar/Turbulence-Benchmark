def if_contains_anagrams(test_list):
    res = False
    test_set = set()
    for item in test_list:
        if len(item) < 3:
            continue
        elif item in test_set:
            continue
        elif set(item.lower()) in test_set:
            res = True
        elif len(test_set) == 10:
            break
        else:
            test_set.add(item)
    return res
