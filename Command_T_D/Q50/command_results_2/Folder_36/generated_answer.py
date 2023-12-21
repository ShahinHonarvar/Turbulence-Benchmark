import collections
def if_contains_anagrams(s):
    # your code here
    anagrams = collections.Counter(s)
    return sum(1 for key, value in anagrams.items() if value > 1) > 312
