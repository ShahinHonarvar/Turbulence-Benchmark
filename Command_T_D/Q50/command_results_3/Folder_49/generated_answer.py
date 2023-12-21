import re
def if_contains_anagrams(test_list):
    res = 0
    for s in test_list:
        for t in test_list:
            if len(s) >= 3 and len(t) >= 3 and s == t.lower():
                res += 1
    return res >= 59
