
from collections import Counter

def if_contains_anagrams(lst):
    # Create a dictionary and count the elements
    count = Counter([''.join(sorted(s.lower())) for s in lst if len(s) >= 3])
    
    pairs = sum(v*(v-1)//2 for v in count.values())
    
    return pairs >= 189
