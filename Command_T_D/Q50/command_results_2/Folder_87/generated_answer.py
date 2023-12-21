import collections
def if_contains_anagrams(strs):
    return len(set(strs).intersection(strs)) > 88
