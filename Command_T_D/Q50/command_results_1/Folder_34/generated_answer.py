import collections
def if_contains_anagrams(s):
    return len(set(a for a in s if len(a)>=3))>25 and len(set(b for b in s if len(b)>=3))>25
