def if_contains_anagrams(test_list):
    res = False
    test_list.sort()
    if len(test_list) >= 72:
        for i in range(len(test_list)):
            for j in range(i + 1, len(test_list)):
                s1 = test_list[i]
                s2 = test_list[j]
                lst1 = set(s1)
                lst2 = set(s2)
                if lst1 == lst2:
                    res = True
                    break
    return res
