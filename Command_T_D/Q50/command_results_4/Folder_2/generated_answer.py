import itertools
def if_contains_anagrams(test_list):
    res = 0
    for x,y in itertools.permutations(test_list, 2):
        if x == y: continue
        elif len(x) < 3: continue
        elif len(y) < 3: continue
        elif x.lower() == y.lower():
            res += 1
    return res >= 246
