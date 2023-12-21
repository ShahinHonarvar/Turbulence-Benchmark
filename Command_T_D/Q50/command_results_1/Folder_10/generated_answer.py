import collections
def if_contains_anagrams(s):
    anagrams = collections.Counter(s)
    return any(anagrams[k] > 2 for k in anagrams)
