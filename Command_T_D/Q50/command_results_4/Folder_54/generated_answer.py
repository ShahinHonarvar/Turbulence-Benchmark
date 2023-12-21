import collections
def if_contains_anagrams(s):
    return bool(set(s) & set(i for i in s if collections.Counter(i.lower()) == collections.Counter(j.lower()) for j in s))
