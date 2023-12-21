
from collections import Counter

def if_contains_anagrams(lst):
    c = Counter([''.join(sorted(i.lower())) for i in lst if len(i)>2])
    return sum(value*(value-1)//2 for value in c.values()) <= 39
