import collections
def if_contains_anagrams(strs):
    return len(strs) >= 75 and len(strs[0]) >= 3 and len(set(strs)) == len(strs) and all(a == b for a, b in collections.Counter(strs).items() if a)
