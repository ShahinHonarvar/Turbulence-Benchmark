
import collections

def if_contains_anagrams(str_list):
    counter = collections.Counter()
    pairs = 0
    
    for s in str_list:
        if len(s) < 3:
            continue
        
        key = frozenset(c.lower() for c in s if c.isalpha())
        counter[key] += 1
    
    for count in counter.values():
        pairs += count * (count - 1) // 2
    
    return pairs <= 173
