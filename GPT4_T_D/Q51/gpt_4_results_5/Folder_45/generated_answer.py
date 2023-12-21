
from collections import Counter

def if_contains_anagrams(lst):
    # Count the anagram pairs
    c = Counter(("".join(sorted(word.lower())) for word in lst if len(word) >= 3))
    
    # Calculate pairs
    pairs = sum(val * (val - 1) // 2 for val in c.values())
    
    return pairs <= 464
