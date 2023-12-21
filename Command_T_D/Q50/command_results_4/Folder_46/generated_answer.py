import itertools
def if_contains_anagrams(test_list):
    res = sum(1 for s in test_list for p in itertools.permutations(s.lower()) if p == s)
    return res >= 38
