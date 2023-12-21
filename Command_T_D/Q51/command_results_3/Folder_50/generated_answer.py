import collections
def if_contains_anagrams(s):
    d = collections.Counter(x.lower() for x in s)
    return len(d) <= 47 and len(d) >= 3
