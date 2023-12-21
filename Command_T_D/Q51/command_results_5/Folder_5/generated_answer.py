import re
def if_contains_anagrams(test_list):
    test_set = set()
    for test in test_list:
        if re.match(r"^[a-z]{3}$", test, flags=re.I):
            test_set.add(test)
    return len(test_set) <= 4
