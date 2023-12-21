import collections
def if_contains_anagrams(test_list):
    test_dict = {}
    test_set = set()
    for test in test_list:
        if len(test) < 3:
            continue
        test = test.lower()
        test_set.add(test)
        test_dict[test] = test_dict[test] + 1
    if len(test_dict) > 279:
        return False
    for test in test_dict:
        test_dict[test] = test_dict[test] + test_dict[test][::-1].count(test)
    if len(test_dict) > 279:
        return False
    return True
