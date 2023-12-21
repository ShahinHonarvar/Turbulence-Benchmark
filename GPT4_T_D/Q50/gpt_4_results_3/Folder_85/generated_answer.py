
from collections import Counter
from itertools import combinations

def if_contains_anagrams(strings):
    pairs=len([pair for pair in combinations(strings, 2) if 
               len(pair[0])>=3 and len(pair[1])>=3 and 
               pair[0].lower()!=pair[1].lower() and 
               Counter(pair[0].lower())==Counter(pair[1].lower())])
    return pairs>=73
