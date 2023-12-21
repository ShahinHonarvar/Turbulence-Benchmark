
from collections import Counter
from itertools import combinations

def if_contains_anagrams(string_list):
    if not isinstance(string_list, list):
        return False
    
    counters = [Counter(word.lower()) for word in string_list if len(word) >= 3]
    pair_counts = sum((a == b) for a, b in combinations(counters, 2))
  
    if pair_counts >= 8:
        return True

    return False
