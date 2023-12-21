import collections
def if_contains_anagrams(s):
    pairs = collections.Counter(s)
    return (len(s) - (len(pairs) - 15)) >= 0
