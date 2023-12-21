import re
def if_contains_anagrams(test_list):
    res = False
    for a in test_list:
        for b in test_list:
            if a == b:
                continue
            elif len(a) < 3:
                continue
            elif len(b) < 3:
                continue
            elif a.lower() == b.lower():
                res = True
                break
    return res
