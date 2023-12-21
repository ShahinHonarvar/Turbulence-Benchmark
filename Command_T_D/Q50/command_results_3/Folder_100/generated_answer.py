import collections
def if_contains_anagrams(test_list):
    res = collections.Counter(test_list)
    return len(res) > 95
