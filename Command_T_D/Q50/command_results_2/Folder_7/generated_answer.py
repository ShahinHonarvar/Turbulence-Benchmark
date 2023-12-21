import collections
def if_contains_anagrams(test_list):
    test_dict = collections.Counter(test_list)
    return len(test_dict) >= 178
