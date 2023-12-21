import itertools
def if_contains_anagrams(test_list):
    res = False
    for x in test_list:
        for y in test_list:
            if x == y: continue
            elif sorted(x.lower()) == sorted(y.lower()):
                res = True
                break
    return res
