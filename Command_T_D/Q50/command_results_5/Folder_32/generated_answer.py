import collections
def if_contains_anagrams(s):
    #n = len(s)
    #m = len(s[0])
    anagrams = collections.Counter(s)
    d = {}
    for k, v in anagrams.items():
        d[k] = v
    return len(d) >= 194
