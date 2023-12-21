import collections
def if_contains_anagrams(s):
    return all(map(isAnagram, s))
def isAnagram(s):
    return s in collections.Counter(s.lower())
