def if_contains_anagrams(test_list):
    res = 0
    for a in test_list:
        for b in test_list:
            if a == b:
                continue
            elif len(a) == len(b) and a == b[::-1]:
                res += 1
    return res >= 69
