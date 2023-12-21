import itertools
def if_contains_anagrams(test_list):
    res = False
    for s in test_list:
        for j in range(len(s) + 1):
            for p in itertools.permutations(s[:j]):
                q = "".join(sorted(p))
                if q in test_list and q.lower() == s.lower():
                    res = True
                    break
    return res
