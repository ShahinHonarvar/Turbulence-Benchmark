import collections
def if_contains_anagrams(str_list):
    anagrams = collections.Counter(s for s in str_list if len(s) >= 3)
    return bool(anagrams.keys())
