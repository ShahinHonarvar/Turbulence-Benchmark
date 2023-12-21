def if_contains_anagrams(test_list):
    res = 0
    for s in test_list:
        res += sum(a == b for a, b in zip(s.lower(), s.lower()))
    return res >= 60
