import re
def if_contains_anagrams(test_list):
    res = True
    for s in test_list:
        for e in test_list:
            if s == e:
                continue
            elif len(s) < 3:
                continue
            elif s == e.lower():
                res = False
                break
            elif s[1:] == e[1:]:
                res = False
                break
            elif s[0] == e[0] and s[2:] == e[2:]:
                res = False
                break
    return res
