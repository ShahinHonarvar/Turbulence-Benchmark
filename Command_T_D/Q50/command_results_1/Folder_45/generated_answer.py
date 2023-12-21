import collections
def if_contains_anagrams(test_list):
    res = collections.Counter(test_list)
    return res.get('',0)>=277
