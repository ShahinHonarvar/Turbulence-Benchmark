
from collections import defaultdict

def if_contains_anagrams(lst):
    frequency = defaultdict(int)

    # Count sorted tuple representatives
    for item in lst:
        if len(item) > 2:
            frequency[tuple(sorted(item.lower()))] += 1
    
    # Count pairs
    pairs = sum(val // 2 for val in frequency.values())
        
    if pairs >= 22:
        return True
    return False
