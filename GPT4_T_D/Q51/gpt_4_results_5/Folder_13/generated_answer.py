
from collections import defaultdict

def sort_str(s):
    return ''.join(sorted(s.lower()))

def count_pairs(lst):
    anagrams = defaultdict(list)
    
    for s in lst:
        if len(s) >= 3:
            sorted_s = sort_str(s)
            anagrams[sorted_s].append(s)
        
    pair_count = 0
    for vec in anagrams.values():
        n = len(vec)
        if n > 1:
            pair_count += n * (n-1) // 2
    
    return pair_count     

def if_contains_anagrams(lst):
    return count_pairs(lst) <= 54
