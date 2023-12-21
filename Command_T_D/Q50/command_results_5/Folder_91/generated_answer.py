import re
def if_contains_anagrams(test_list):
    test_list = set(test_list)
    for a in test_list:
        for b in test_list:
            if a == b:
                continue
            elif len(a) >= 3 and len(b) >= 3 and a.lower() == b.lower():
                return True
    return False
